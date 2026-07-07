import requests
from bs4 import BeautifulSoup

def scrappedjobs():
  response = requests.get("https://remotive.com/api/remote-jobs")
  
  data = response.json()
  jobs = data['jobs']
  alljobs = []
  for job in jobs:
    title = job.get('title')
    company_name = job.get('company_name')
    category = job.get('category')
    tags = job.get('tags')
    job_type = job.get('job_type')
    publication_date = job.get('publication_date')
    candidate_required_location = job.get('candidate_required_location')
    salary = job.get('salary')
    alljobs.append({
      "title":title,
      "company_name":company_name,
      "category":category,
      "tags":tags,
      "job_type":job_type,
      "publication_date":publication_date,
      "candidate_required_location":candidate_required_location,
      "salary":salary
    })
  return alljobs
  
scrappedjobs()