# this is step 3
from bs4 import BeautifulSoup
import requests

def finder(url):
    
    soup = BeautifulSoup(requests.post(url).text, "html.parser")

    button_elements = soup.find_all('button', class_='timer-button')

    links=[]
    # Extract the data-redirect attribute
    for button_element in button_elements:
        data_redirect = button_element.get('data-redirect')
        links.append(data_redirect)
    else:
        print("Button element with class 'timer-button' not found.")
    
    return links
def main():
    linkse=finder('https://download.howtofree.org/the-ultimate-dark-web-anonymity-privacy-security-course-download-1/')
    print(linkse)
    
if __name__=="__main__":
    main()