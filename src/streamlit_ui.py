import streamlit as st

from models.course import Course, SearchResult


def course_card(course: Course):
    with st.container():
        st.markdown(f"""
        <div class="course-card">
            <img src={course.image} alt="{course.title}" style="max-width: 100%; height: auto; border-radius: 8px;" />
            <h3>{course.title}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("View Curriculums"):
            for i, curriculum in enumerate(course.curriculums, start=1):
                st.markdown(f"{i}. {curriculum}")

def search_results(result: SearchResult):
    st.subheader(f"Search Results for: '{result.query}'")
    if result.courses:
        for i, course in enumerate(result.courses, 1):
            st.write(f"Result {i}:")
            course_card(course)
    else:
        st.info("No courses found matching your query. Try different search terms!")

def sidebar():
    with st.sidebar:
        st.header("About")
        st.write("""
        This tool helps you find free courses on Analytics Vidhya using natural language search.
        Simply type what you're looking for, and we'll find the most relevant courses for you!
        """)
        
        st.header("Examples")
        st.write("""
        Try searching for:
        - Machine learning courses for beginners
        - Advanced Python programming
        - Data visualization tutorials
        - Deep learning projects
        """)

