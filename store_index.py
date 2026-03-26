from dotenv import load_dotenv
import os
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from src.helper import load_pdf_files, filter_to_min_docs, text_split, download_embedding

load_dotenv()

Pinecone_api_key = os.getenv("PINECONE_API_KEY")

extracted_data = load_pdf_files("data/")
filtered_data = filter_to_min_docs(extracted_data)
chunks = text_split(filtered_data)

embeddings = download_embedding()

pc = Pinecone(Pinecone_api_key)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension = 384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws",region="us-east-1")
    )

index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    index_name=index_name
)
