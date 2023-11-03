from bs4 import BeautifulSoup
import requests
# this is use to reach perticular course
# html = ""
# with open("index5.html", "r") as f:
#     html = f.read()
html=requests.post('https://www.howtofree.org/complete-networking-fundamentals-course-4/').text
soup = BeautifulSoup(html, "html.parser")

element = soup.find_all(id='course-link')

# print(element)
print(element['href'])