from sentence_transformers import SentenceTransformer
from backend.services.pinecone_client import init_pinecone

model = SentenceTransformer("all-MiniLM-L6-v2")
index = init_pinecone()

def search_policies(query: str, top_k=5):
    query_embedding = model.encode([query]).tolist()[0]
    results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)

    return [match["metadata"]["text"] for match in results["matches"]]
