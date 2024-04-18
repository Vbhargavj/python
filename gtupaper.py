import requests
import os


def download_pdf(year, code):

    url = f"https://www.gtu.ac.in/uploads/{year}/BE/{code}.pdf"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        filename = f"{year}-{code}.pdf"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"File {filename} downloaded successfully.")
    else:
        print("Failed to download the file.")


if __name__ == "__main__":
    years = ["W2023", "W2022", "W2021", "S2023", "S2022", "S2021"]
    code = input("Enter the code (e.g., 3161608): ")

    for year in years:
        download_pdf(year, code)
