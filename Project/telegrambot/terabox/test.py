import requests
url="https://reelsave.app/terabox"

response=requests.get(url)

data=response.text



with open("collecssdt_tara_data.html", "w",encoding='utf-8') as f:
    f.write(data)
