# that is first step
from bs4 import BeautifulSoup
import requests
import re

def extract_course_info(url):
    
    soup = BeautifulSoup(requests.post(url).text, "html.parser")

    
    articles = soup.find_all("article")
    course_info_list = []
    author_tags = soup.find_all('p', class_='has-text-align-center')

    for author_tag, article in zip(author_tags, articles):
        values = author_tag.text.split(' ')
        if "Author" in values:
            author_text = ' '.join(values)
            cleaned_text = re.sub(r'\s+', ' ', author_text).strip()
            author_name = cleaned_text.split(' : ')[1]

            title_element = article.find("h2", class_="entry-title")
            title = title_element.get_text() if title_element else "Title not found"

            img_element = article.find("div", class_="post-image").find("img")
            img_src = img_element.get("src") if img_element else "Image src not found"

            link_element = title_element.find("a")
            course_link = link_element.get("href") if link_element else "Course link not found"

            course_info = {
                "Title": title.strip(),
                "Course Link": course_link,
                "Img src": img_src,
                "Author": author_name
            }
            course_info_list.append(course_info)

    return course_info_list
def main():
    
    courses=(extract_course_info(requests.post('https://www.howtofree.org/category/cyber-security-courses/').text))
    for coure in courses:
        print("Title ",coure["Title"])
    print(courses)
if __name__=='__main__':
    main()
