from flask import Flask, request, jsonify, render_template
from src.helper import download_embedding
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from src.prompt import *

load_dotenv()

app = Flask(__name__)


embeddings = download_embedding()

index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    embedding=embeddings,
    index_name=index_name
)

retriver = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

llm = ChatGroq(model="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", sys_prompt),
        ("human", "{input}")
    ]
)

qna_chain = create_stuff_documents_chain(llm,prompt)
rag_chain = create_retrieval_chain(retriver,qna_chain)


@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET","POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input":input})
    print(response['answer'])
    return str(response['answer'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080 ,debug=True)


