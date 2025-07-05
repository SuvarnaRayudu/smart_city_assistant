from pydantic import BaseSettings

class Settings(BaseSettings):
    watsonx_api_key: str
    watsonx_project_id: str
    watsonx_model_id: str
    pinecone_api_key: str
    pinecone_env: str
    pinecone_index: str

    class Config:
        env_file = ".env"

settings = Settings()
