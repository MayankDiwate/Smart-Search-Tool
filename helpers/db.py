import os
from typing import List

import streamlit as st
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone, ServerlessSpec

from models.course import Course


# Initialize Pinecone
@st.cache_resource
def init_pinecone():
    # Retrieve API key and environment from Streamlit secrets
    api_key = st.secrets['secrets']["PINECONE_API_KEY"]
    api_host = st.secrets['secrets']["PINECONE_API_HOST"]

    os.environ["PINECONE_API_KEY"] = api_key 
    os.environ["PINECONE_API_HOST"] = api_host
    print('Pinecone API key:', api_key)

    # Create Pinecone instance
    pc = Pinecone(api_key=api_key)
    
    # Example: Create an index if it doesn't exist
    if 'courses' not in pc.list_indexes().names():
        pc.create_index(
            name='courses',
            dimension=1024,
            metric='euclidean',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
    return pc

@st.cache_resource
def initialize_vector_store(_courses: List[Course]):
    """
    Initialize and populate Pinecone vector store
    """
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-large-en-v1.5",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Create Pinecone index
        index_name = "courses"
        
        # Create vector store using langchain's Pinecone class
        vector_store = LangchainPinecone.from_existing_index(
            index_name=index_name, 
            embedding=embeddings,
            text_key="text"
        )
        
        # Now insert the documents
        vector_store.add_texts(
            texts=[course.title for course in _courses],
            metadatas=[{"title": course.title, "curriculums": course.curriculums} for course in _courses]
        )

        st.toast("Data stored in Pinecone successfully!", icon="🔥")
        
        return vector_store
    except Exception as e:
        st.error(f"Error initializing vector store: {str(e)}")
        return None