# this is step2

from bs4 import BeautifulSoup
import requests

def downla(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    elements = soup.find_all(id='course-link')

    for element in elements:
        link = element.get('href')
        if link:
            return link

def main():
    print(downla('https://www.howtofree.org/complete-networking-fundamentals-course-4/'))

if __name__ == "__main__":
    main()
