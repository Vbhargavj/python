from bs4 import BeautifulSoup
import re

# this is for extrating all the course here extract the title,course link and img link 
# Sample HTML
html = ""
with open("collect_data.html", "r") as f:
    html = f.read()
print('done')
# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all article elements with class "post"
articles = soup.find_all("article")
with open("collected_data.txt", "w") as f:
    for article in articles:
        # Extract the title
        title_element = article.find("h2", class_="entry-title")
        if title_element:
            title = title_element.get_text()
        else:
            title = "Title not found"

        # Extract the img src
        img_element = article.find("div", class_="post-image").find("img")
        if img_element:
            img_src = img_element.get("src")
        else:
            img_src = "Image src not found"

        # Extract the course link
        link_element = title_element.find("a")
        if link_element:
            course_link = link_element.get("href")
        else:
            course_link = "Course link not found"

        # Print the extracted information
        title = re.sub(r"\s+", " ", title)
        f.write("Title: " + title + "\n")
        f.write("Img src: " + img_src + "\n")
        f.write("Course link: " + course_link + "\n\n")
