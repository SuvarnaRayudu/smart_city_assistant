import pinecone
from backend.core.config import settings

def init_pinecone():
    pinecone.init(api_key=settings.pinecone_api_key, environment=settings.pinecone_env)
    if settings.pinecone_index not in pinecone.list_indexes():
        pinecone.create_index(name=settings.pinecone_index, dimension=384)
    return pinecone.Index(settings.pinecone_index)
