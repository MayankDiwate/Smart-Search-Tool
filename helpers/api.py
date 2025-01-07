import requests
from bs4 import BeautifulSoup

from utils import convert_to_url_format


def parse_products():
    products = []
    for page in range(1, 10):
        url = f"https://courses.analyticsvidhya.com/collections/courses?page={page}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        products.append(soup.find_all('li', class_='products__list-item'))
        flat_products = [product for page in products for product in page]

    return flat_products

import requests
from bs4 import BeautifulSoup


def get_course_details(course_link):
    try:
        course_link = convert_to_url_format(course_link)
        url = f"https://courses.analyticsvidhya.com/{course_link}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        curriculums = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            course_curriculums = soup.body.find_all('h5', class_='course-curriculum__chapter-title')

            print('Course curriculums' ,course_curriculums)

            for curriculum in course_curriculums:
                curriculum_title = curriculum.text.strip()
                if curriculum_title:
                    print(curriculum_title)
                    curriculums.append(curriculum_title)
                # curriculum_title = curriculum.find('header', class_='course-curriculum__chapter-header')

        return curriculums

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"404 Error: Course not found for link: {course_link}")
        else:
            print(f"HTTP Error for link {course_link}: {http_err}")
        return []

    except requests.exceptions.RequestException as req_err:
        print(f"Request Exception for link {course_link}: {req_err}")
        return []