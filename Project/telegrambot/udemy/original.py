from bs4 import BeautifulSoup

html = ""
with open("index6.html", "r") as f:
    html = f.read()
    
soup = BeautifulSoup(html, "html.parser")

origin_link=soup.find('a',{'data-type': 'link'}).get('href')


