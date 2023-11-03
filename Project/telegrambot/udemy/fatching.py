import requests 

url='https://www.howtofree.org/category/web-appliciation/'

response=requests.post(url)

data=response.text



with open("collect_data.html", "w") as f:
    f.write(data)
