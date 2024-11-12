# Intelligent Document Query System with LLM-Powered RAG

## Overview

The **Intelligent Document Query System** is a custom Retrieval-Augmented Generation (RAG) system that allows users to query documents intelligently. Users can upload documents (PDFs or URLs) for analysis and retrieval, which are then stored in a vector database for fast and accurate response generation. This project combines the power of multiple Large Language Models (LLMs), a vector database (AstraDB), and a web interface built with Streamlit, providing a robust and efficient querying tool. 

## Key Features

- **Document Input**: Users can upload PDFs or provide URLs, which are processed and chunked for efficient storage and retrieval.
- **LLM-Powered RAG**: Utilizes multiple LLMs and LangChain to generate concise, accurate responses based on stored document data.
- **Vector Database Storage**: Data chunks are stored in AstraDB’s vector database, optimizing retrieval accuracy and speed while reducing costs.
- **REST API Integration**: The backend is powered by Flask, exposing REST API endpoints to handle data flow, processing, and querying.
- **User-Friendly Interface**: Streamlit provides a simple yet effective front-end for document input and response viewing.

## Technology Stack

- **Python**: Primary language used for data processing, backend, and integration.
- **Flask**: REST API framework to manage backend services and facilitate communication between the front end and data storage.
- **Streamlit**: Front-end framework used to create a clean, interactive UI.
- **LangChain**: Framework to integrate multiple LLMs, managing prompt chains for dynamic response generation.
- **AstraDB**: Vector database used for storing and retrieving chunked document data.
- **LLMs**: Multiple large language models are used to optimize response accuracy.

## Project Architecture

1. **Data Ingestion**: 
   - PDFs or URLs are provided as input, then parsed, chunked, and stored in AstraDB.
   
2. **Data Storage**: 
   - Each document is stored in AstraDB’s vector database, facilitating fast and accurate retrieval based on similarity searches.
   
3. **Query Handling**:
   - Users input queries via the Streamlit UI. Queries are processed by the Flask REST API, which retrieves relevant data chunks from AstraDB.
   
4. **Response Generation**:
   - Retrieved data chunks are passed through LangChain, where multiple LLMs work together to generate user-friendly, accurate responses.

## Installation

To get started, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/intelligent-document-query-system.git
   cd intelligent-document-query-system

2. **Create a Virtual Environment**:
   ```bash
    python3 -m venv env
    source env/bin/activate  # For Windows, use 'env\Scripts\activate'

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. Set Up AstraDB and API Keys:
    Set up an account with AstraDB and obtain an API key.
    Add any necessary API keys for LLMs in a .env file, like:
     ```bash
     ASTRA_DB_API_KEY=<your_astradb_api_key>
     LLM_API_KEY=<your_llm_api_key>

5. Run the Flask REST API:
   ```bash
   python restapi.py

6. Run the app
   ```bash
   streamlit run app.py

## Usage
1. Upload Documents:
    Open the Streamlit interface and upload a PDF or input a URL to be processed.
2. Query the Document:
    Use the query interface to ask questions related to the uploaded document. The system will retrieve and analyze relevant chunks to generate an answer.
3. View Results:
    Responses will be displayed in the Streamlit interface, showing an intelligently generated answer based on your query.
