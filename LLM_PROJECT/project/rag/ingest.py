import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import pickle

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
with open("rag/data.json", "r") as f:
    data = json.load(f)

documents = []
for item in data:
    documents.append(item["content"])

# Generate embeddings
embeddings = model.encode(documents)

# Convert to numpy
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
os.makedirs("rag/vector_store", exist_ok=True)
faiss.write_index(index, "rag/vector_store/index.faiss")

# Save documents separately
with open("rag/vector_store/documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("✅ FAISS index created successfully!")
