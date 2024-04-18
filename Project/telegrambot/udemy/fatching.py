import requests

url = "https://mkvcinemas.mov/leo-2023/"

response = requests.post(url)

data = response.text


with open("collect_movie_data.html", "w") as f:
    f.write(data)
