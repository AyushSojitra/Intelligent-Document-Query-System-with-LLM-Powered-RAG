import streamlit as st
from PyPDF2 import PdfReader
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_community.llms import OpenAI
import cassio
from langchain_community.embeddings import OpenAIEmbeddings
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

db_id = "your_db_id"
db_endpoint = "your_db_endpoint"
db_token = "your_db_token"


def processPDF(input):
    truncateDB()
    pdf = PdfReader(input)
    text = ""
    for page in pdf.pages:
        text+=page.extract_text() + "\n"
    store(text)

def processURL(input):
    truncateDB()
    loader = UnstructuredURLLoader(urls=[input])
    text = loader.load()
    store(str(text))

def truncateDB():
    SECURE_CONNECT_BUNDLE_PATH = "SECURE_CONNECT_BUNDLE_PATH"
    ASTRA_DB_CLIENT_ID = "ASTRA_DB_CLIENT_ID"
    ASTRA_DB_CLIENT_SECRET = "ASTRA_DB_CLIENT_SECRET"
    KEYSPACE = 'KEYSPACE'
    auth_provider = PlainTextAuthProvider(
        username=ASTRA_DB_CLIENT_ID, 
        password=ASTRA_DB_CLIENT_SECRET
    )
    cluster = Cluster(
        cloud={'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH}, 
        auth_provider=auth_provider
    )
    session = cluster.connect(KEYSPACE)
    truncate_query = "TRUNCATE vectors"
    session.execute(truncate_query)

    print("Table 'vectors' has been truncated successfully.")
    session.shutdown()


def store(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    embeddings = OpenAIEmbeddings(openai_api_key="openai_api_key")
    cassio.init(token = db_token,
               database_id = db_id)
    vectorStore = Cassandra(
       embedding = embeddings,
       table_name = 'vectors',
       keyspace = 'pdf_vectors',
       session = None
    )
    vectorStore.add_texts(chunks)
    global vectorIndex
    vectorIndex = VectorStoreIndexWrapper(vectorstore = vectorStore)
    st.write("Database Updated")

def get_response(query):
    model = OpenAI(openai_api_key="openai_api_key")
    result = vectorIndex.query(query, llm=model)
    return result