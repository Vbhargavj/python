from bs4 import BeautifulSoup
import requests
html = ""
# with open("index6.html", "r") as f:
#     html = f.read()
html=html=requests.post('https://download.howtofree.org/the-complete-networking-fundamentals-course-your-ccna-start/').text
soup = BeautifulSoup(html, "html.parser")

button_elements = soup.find_all('button', class_='timer-button')
links=[]
# Extract the data-redirect attribute
for button_element in button_elements:
    data_redirect = button_element.get('data-redirect')
    links.append(data_redirect) 
else:
    print("Button element with class 'timer-button' not found.")