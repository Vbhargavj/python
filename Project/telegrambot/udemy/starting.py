# import requests as req

# url = "https://www.howtofree.org/category/cyber-security-courses/"

# data=req.post(url).text

# with open("D:\coding\Code\python\index.html", "w") as f:
#     f.write(data)
html_doc = ""
with open("D:\coding\Code\python\index.html", "r") as f:
    html_doc = f.read()


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

# for link in soup.find_all('a'):
#     if(link.parent.name=='div'):
#         print(link.get('href'))

# Find all divs with class "post-image"
divs = soup.find_all(class_="post-image")
entry_divs=soup.find_all('h2',class_='entry-title')
with open('collect_data.txt','w') as f :
# Loop through each "post-image" div and extract links
    for div in divs:
    # Find the link inside the div
        link = div.find('a')
        src_link=link_url=''
    # Extract the 'href' attribute from the link
        if link:
            link_url = link.get('href')
            print(link_url)
    
    # Find the img tag inside the div
        img_tag = div.find("img")

        if img_tag:
            src_link = img_tag.get("src")
            print(src_link)
    
        f.write("Course link: " + link_url + "\n")
        f.write("Image link: " + src_link + "\n")
    

    
entry_divs=soup.find_all('h2',class_='entry-title')

for entry_div in entry_divs:
    title = entry_div.get_text()
    print(title)
# for content in entry_divs:
#     link=content.find('')