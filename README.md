# Project Overview
The Sustainable Smart City Assistant is an AI-powered platform to support urban sustainability,
governance, and citizen engagement. It combines IBM Watsonx Granite LLM, Streamlit, FastAPI,
and Pinecone to provide services like policy summarization, KPI forecasting, eco tips, feedback
handling, and anomaly detection.

# Tech Stack
- IBM Watsonx Granite LLM (text summarization, chat, eco tips)
- Pinecone (semantic vector search for policies)
- Streamlit (interactive frontend dashboard)
- FastAPI (modular backend API)
- Scikit-learn (KPI forecasting)
- SentenceTransformers (document embedding)
- dotenv + pydantic (env config)

# Modules Implemented
1. Policy Summarization (Granite LLM)
2. KPI Forecasting (Linear Regression)
3. Anomaly Detection (Z-score Method)
4. Chat Assistant (LLM queries)
5. Eco Tips Generator (LLM keywords)
6. Citizen Feedback Logging (with category tags)
7. Semantic Policy Search (Pinecone + Embeddings)

# Project Workflow
- Users interact via Streamlit UI.
- Backend routes handle logic using FastAPI.
- LLMs generate text, summaries, tips & chat responses.
- Vector search handled by Pinecone.
- Responses rendered on UI with toast messages & cards.

# Development Phases
1. Phase 1 - Project Setup with Modular Structure
2. Phase 2 - IBM Watsonx Granite LLM Integration
3. Phase 3 - API Routes (Chat, Feedback, KPI, Anomaly)
4. Phase 4 - Streamlit UI Dashboard + Components
5. Phase 5 - Pinecone Semantic Search + Embedding