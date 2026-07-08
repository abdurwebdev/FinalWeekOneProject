import requests

def get_jobs_from_remotive():
  response = requests.get("https://remotive.com/api/remote-jobs")
  
  return response.json()