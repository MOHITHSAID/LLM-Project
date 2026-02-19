from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB
db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)


# Test query
query = "Tell me about Taj Mahal"

results = db.similarity_search(query, k=3)

for i, doc in enumerate(results):
    print("\nResult", i+1)
    print(doc.page_content)
