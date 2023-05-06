from bs4 import BeautifulSoup

with open('home.html','r') as file:
    content = file.read()

    soup = BeautifulSoup(content,'lxml')

    course_card = soup.find_all('div', class_='card')
    for course in course_card:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} cost {course_price}')