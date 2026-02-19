from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB
db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)


# Retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)

print("Monument AI Assistant Ready!")
print("Type 'exit' to quit.")

while True:
    query = input("\nAsk: ")

    if query.lower() == "exit":
        break

    answer = qa_chain.run(query)
    print("\nAnswer:", answer)
