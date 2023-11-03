# this is step 2
from bs4 import BeautifulSoup
import requests
import re
html = ""
# with open("index.html", "r") as f:
#     html = f.read()
    
# soup = BeautifulSoup(html, "html.parser")
    
# origin_link=soup.find('a',{'data-type': 'link'}).get('href')


def original(url):
    soup=BeautifulSoup(requests.post(url).text,'html.parser')
    origin_link=soup.find('a',{'data-type': 'link'}).get('href')
    return origin_link

def main():
    print(original('https://download.howtofree.org/the-ultimate-dark-web-anonymity-privacy-security-course-download-1/'))

# 8(*********************)only use this
def original2(url):
    # html=''
    # with open("D:\\coding\\Code\\python\\Project\\telegrambot\\udemy\\bot\\index3.html", "r") as f:
    #     html = f.read()
    
    soup = BeautifulSoup(requests.post(url).text, "html.parser")
    author_tags = soup.find_all('p', class_='has-text-align-center')
    # print(author_tags)
    for author_tag in author_tags:
        values = author_tag.text.split(' ')
        if "Author" in values:
            author_text = ' '.join(values)
            cleaned_text = re.sub(r'\s+', ' ', author_text).strip()
            print(cleaned_text.split(' : ')[1])
               
    
    
if __name__=="__main__":
    original2()