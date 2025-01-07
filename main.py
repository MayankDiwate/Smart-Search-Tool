import streamlit as st

from helpers.courses import scrape_courses, search_courses
from helpers.db import init_pinecone, initialize_vector_store
from src.streamlit_ui import search_results, sidebar

# Page configuration
st.set_page_config(
    page_title="Analytics Vidhya Course Search",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
    }
    .course-card {
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e0e0e0;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)



# Main app
def main():
    st.title("📚 Analytics Vidhya Course Search")
    col1, col2 = st.columns([6, 1])

    with col1:
        st.write("Find the perfect free course using natural language search")

    with col2:
        if st.button("Scrape Data", key="scrape_data"):
            courses = scrape_courses()

    # Initialize Pinecone
    init_pinecone()
    
    # Render sidebar
    sidebar()
    
    # Initialize or get vector store from session state
    if 'vector_store' not in st.session_state:
        with st.spinner("🔄 Initializing search system..."):
            courses = scrape_courses()
            if courses:
                st.session_state.vector_store = initialize_vector_store(courses)
            else:
                st.error("Unable to fetch courses. Please try again later.")
                return

    # Search interface
    query = st.text_input("🔍 What would you like to learn?", 
                         placeholder="E.g., machine learning for beginners")
    
    if query:
        with st.spinner("🔍 Searching for relevant courses..."):
            result = search_courses(query, st.session_state.vector_store)
            search_results(result)

if __name__ == "__main__":
    main()

