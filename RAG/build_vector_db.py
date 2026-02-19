import os
import warnings
warnings.filterwarnings('ignore')
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Step 1 — Load documents
data_folder = "data"
docs = []

for file in os.listdir(data_folder):
    if file.endswith(".txt"):
        loader = TextLoader(
        os.path.join(data_folder, file),
        encoding="utf-8"
        )

        docs.extend(loader.load())

print("Documents loaded:", len(docs))


# Step 2 — Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=80
)

documents = text_splitter.split_documents(docs)

print("Chunks created:", len(documents))


# Step 3 — Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Step 4 — Create FAISS vector DB
vector_db = FAISS.from_documents(documents, embeddings)


# Step 5 — Save vector DB
vector_db.save_local("vector_db")

print("Vector DB successfully created!")
