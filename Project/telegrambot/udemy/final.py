from bs4 import BeautifulSoup
import requests
import re


def fatch_1(url):
    data = requests.post(url).text
    titles = []
    link_1 = []
    img = []

    soup = BeautifulSoup(data, "html.parser")
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
            print(title)
            titles.append(title)
            link_1.append(course_link)
            img.append(img_src)
            info_course(titles, link_1, img)


def info_course(titles, link_1, imgs):
    for i, title in enumerate(titles):
        print(f"{i + 1}: {title}")

    


def course():
    print("App Development")
    print("Web Development")
    print("Ethical Hacking")
    print("Web Application")
    print("Cyber Security")
    print("Wifi-Hacking")
    print("Computer Networks")
    print("Video Editing")
    print("Chat-gpt")
    print("Software Development")
    print("Other")

    choise = int(input("Select the number according to the course"))
    if choise == 1:
        url = "https://www.howtofree.org/category/app-development/"
        fatch_1(url)


options = [
    ["App Development"],
    ["Web Development"],
    ["Ethical Hacking"],
    ["Web Application"],
    ["Cyber Security"],
    ["Wifi-Hacking"],
    ["Computer Networks"],
    ["Video Editing"],
    ["Chat-gpt"],
    ["Software Development"],
    ["Other"],
]
# for item in options:
#     print("print('" + item[0] + "')")
if __name__ == "__main__":
    course()
