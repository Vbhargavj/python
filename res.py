import requests

url="https://olamovies.tokyo/generate/?id=106160"

data=requests.post(url)

with open('ola.html','w' ) as f:
    f.write(data.text)