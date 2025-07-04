import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.indeed.com/jobs?q=data+analyst&l=India"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

job_titles, companies, locations, summaries = [], [], [], []

for job in soup.find_all('div', class_='job_seen_beacon'):
    job_titles.append(job.find('h2').text.strip() if job.find('h2') else None)
    companies.append(job.find('span', class_='companyName').text.strip() if job.find('span', class_='companyName') else None)
    locations.append(job.find('div', class_='companyLocation').text.strip() if job.find('div', class_='companyLocation') else None)
    summaries.append(job.find('div', class_='job-snippet').text.strip() if job.find('div', class_='job-snippet') else None)

df = pd.DataFrame({
    'Job Title': job_titles,
    'Company': companies,
    'Location': locations,
    'Summary': summaries
})
df.to_csv("data/job_listings.csv", index=False)
print("Scraped data saved to job_listings.csv")
