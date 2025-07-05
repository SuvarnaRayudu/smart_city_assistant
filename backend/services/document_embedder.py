from sentence_transformers import SentenceTransformer
from backend.services.pinecone_client import init_pinecone

model = SentenceTransformer("all-MiniLM-L6-v2")
index = init_pinecone()

def chunk_text(text, max_chunk_size=300):
    sentences = text.split(".")
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk + sentence) < max_chunk_size:
            chunk += sentence + "."
        else:
            chunks.append(chunk.strip())
            chunk = sentence + "."
    chunks.append(chunk.strip())
    return chunks

def embed_and_store(document_id: str, text: str):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks).tolist()

    to_upsert = [
        (f"{document_id}_{i}", embedding, {"text": chunk})
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings))
    ]
    
    index.upsert(vectors=to_upsert)
    return {"message": f"{len(to_upsert)} chunks embedded and stored"}
