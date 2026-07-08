import requests
from bs4 import BeautifulSoup
from app.scrapper.schemas import StandardJob

def scrape_remotive_jobs():
  response = requests.get("https://remotive.com/api/remote-jobs")
  
  data = response.json()
  jobs = data['jobs']
  alljobs = []
  for job in jobs:
    html_description = job.get('description',"")
    if not html_description:
      continue
    soup = BeautifulSoup(html_description,"html.parser")
    clean_text = soup.get_text(separator = "\n")
    split_lines = clean_text.splitlines()
    clean_text = "\n".join([line.strip() for line in split_lines if line.strip() ]) 
    standard_jobs = StandardJob(
     title = job.get('title'),
    company_name = job.get('company_name'),
    url = job.get('url'),
    category = job.get('category'),
    tags = job.get('tags'),
    job_type = job.get('job_type'),
    company_logo = job.get('company_logo'),
    publication_date = job.get('publication_date'),
    candidate_required_location = job.get('candidate_required_location'),
    salary = job.get('salary'),
    description=clean_text,
    source="Remotive"
    )
    alljobs.append(standard_jobs)
  return alljobs
  