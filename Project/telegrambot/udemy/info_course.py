from bs4 import BeautifulSoup
import re
# for 4 number
# Sample HTML
html = ""
with open("index4.html", "r") as f:
    html = f.read()
print('done')

soup=BeautifulSoup(html, "html.parser")
details=soup.find_all('ul')

ala=details[4].find_all('li')
for item in ala:
    # print(item.find('a')['href'].replace('-',' ').replace('#',''))
    
    # print(item.find('a').get_text())
    # print(item.find('a')['href'][1],end='')
    # print(item.find('a')['href'][2])
    if(item.find('a')['href'].replace('#','')[:1]==re.sub(r"\s+", " ",item.get_text())[:1]):
        print(re.sub(r"\s+", " ",item.get_text()))
        
    if(item.find('a')['href'].replace('#','')[:2]==re.sub(r"\s+", " ",item.get_text())[:2]):
        print(re.sub(r"\s+", " ",item.get_text()))
    # print(item.find('a')['href'].replace('#','')[:2])
    # print(re.sub(r"\s+", " ",item.get_text())[:2])

    