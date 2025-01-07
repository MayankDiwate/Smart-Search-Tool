from typing import List

import streamlit as st

from helpers.api import get_course_details, parse_products
from models.course import Course, SearchResult


def scrape_courses() -> List[Course]:
    """
    Scrape free course information from Analytics Vidhya
    """
    try:
        course_list = parse_products()
        courses=[]

        for course in course_list:
            card_body = course.find('div' , class_='course-card__body')
            if card_body and card_body.find('h3'):
                title = card_body.find('h3').text.strip()
                            
            # card_image = course.find('img', class_='course-card__img')
            # print(card_image)
            # if card_image:    
            #     image = card_image.get('src')

            course_anchor = course.find('a', class_='course-card course-card__public published')
            if course_anchor:
                course_link = course_anchor.get('href')
            
            curriculums = get_course_details(course_link)
            
            course = Course(title=title,image='image',curriculums=curriculums)
            courses.append(course)
            
        return courses
        
    except Exception as e:
        st.error(f"Error scraping courses: {str(e)}")
        # print(f"Error scraping courses: {str(e)}")
        return []

def search_courses(query: str, vector_store) -> SearchResult:
    """
    Search for relevant courses using vector similarity
    """
    try:
        results = vector_store.similarity_search(
            query,
            k=5
        )
        courses = [Course(**doc.metadata) for doc in results]
        return SearchResult(courses=courses, query=query)
    except Exception as e:
        st.error(f"Error searching courses: {str(e)}")
        return SearchResult(courses=[], query=query)