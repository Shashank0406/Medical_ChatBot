import streamlit as st
from src.helper import download_embedding
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *

load_dotenv()

st.set_page_config(page_title="Medical ChatBot", page_icon="🏥")
st.title("🏥 Medical ChatBot")

# ── Load resources once ──────────────────────────────────────────────
@st.cache_resource
def load_rag_chain():
    embeddings = download_embedding()

    docsearch = PineconeVectorStore.from_existing_index(
        embedding=embeddings,
        index_name="medical-chatbot"
    )

    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    llm = ChatGroq(model="llama-3.1-8b-instant")

    prompt = ChatPromptTemplate.from_messages([
        ("system", sys_prompt),
        ("human", "{input}")
    ])

    qna_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, qna_chain)
    return rag_chain

rag_chain = load_rag_chain()

# ── Chat history ─────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── User input ───────────────────────────────────────────────────────
if user_input := st.chat_input("Ask a medical question..."):

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = rag_chain.invoke({"input": user_input})
            answer = response["answer"]
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})