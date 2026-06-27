from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(source.text, "lxml")

data =[]

jobs = soup.find_all("div", class_="card")
for job in jobs:
    title = job.find("h2", class_="title is-5").text
    company = job.find("h3", class_="subtitle is-6 company").text
    location = job.find("p", class_="location").text.strip()

    data.append([
        title,
        company,
        location
    ])

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location"])
    writer.writerows(data)

print(f"Status Code: {source.status_code}")
print(f"Saved {len(data)} jobs to jobs.csv")