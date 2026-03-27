from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings




#Extraxting text from PDF files

def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents

def filter_to_min_docs(docs: List[Document]) -> List[Document]:
    min_doc: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        min_doc.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return min_doc

def text_split(min_docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    chunks = text_splitter.split_documents(min_docs)
    return chunks

def download_embedding():

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedings = HuggingFaceEmbeddings(model_name=model_name)
    return embedings
