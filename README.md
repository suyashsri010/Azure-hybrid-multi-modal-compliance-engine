# Hybrid Multi-Modal Compliance Engine

![Architecture Diagram](./architecture.png)

A backend pipeline built to automate the QA review process for video content. 

Manual video compliance is a bottleneck. This project solves that by taking a raw video source (like a YouTube URL), extracting the speech and on-screen text, and running it against a vectorized database of compliance rules. It uses a LangGraph multi-agent workflow to handle the reasoning and serves the final audit report via a FastAPI endpoint.

## How It Works

1. **Ingestion:** A video is temporarily stored in Azure Blob Storage and processed by **Azure Video Indexer** to extract OCR and transcripts.
2. **Retrieval (RAG):** The system queries **Azure AI Search** (our vector DB) to pull the specific regulatory guidelines relevant to the content.
3. **Evaluation:** **LangGraph** routes the transcript and the rules to **GPT-4o**, which evaluates the claims and flags violations.
4. **Serving & Tracing:** The entire flow is triggered via a **FastAPI** backend, with full LLM tracing and latency monitoring handled by **LangSmith** and **Azure Application Insights**.

## Tech Stack
* **Core:** Python, FastAPI, LangGraph
* **AI/LLM:** OpenAI API (GPT-4o, text-embedding-3-small)
* **Cloud Infrastructure:** Azure Video Indexer, Azure AI Search, Azure Blob Storage
* **Observability:** LangSmith, Azure Application Insights

## Local Setup

### 1. Clone & Install
Ensure you have Python 3.10+ installed.

```bash
git clone [https://github.com/suyashsri010/Azure-hybrid-multi-modal-compliance-engine.git](https://github.com/suyashsri010/Azure-hybrid-multi-modal-compliance-engine.git)
cd Azure-hybrid-multi-modal-compliance-engine
pip install -r requirements.txt

### 2. Environment Variables
Create a .env file in the root directory. You will need active API keys for OpenAI, Azure, and LangSmith.

Code snippet
OPENAI_API_KEY="sk-..."

AZURE_SEARCH_ENDPOINT="..."
AZURE_SEARCH_KEY="..."
AZURE_SEARCH_INDEX_NAME="..."

VI_ACCOUNT_ID="..."
VI_API_KEY="..."
VI_LOCATION="..."

LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY="..."
LANGCHAIN_PROJECT="compliance-engine"
APPLICATIONINSIGHTS_CONNECTION_STRING="..."
