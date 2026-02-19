import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("rag/vector_store/index.faiss")

# Load documents
with open("rag/vector_store/documents.pkl", "rb") as f:
    documents = pickle.load(f)


def retrieve(query, top_k=1):
    # Convert query to embedding
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        results.append(documents[idx])

    return results
