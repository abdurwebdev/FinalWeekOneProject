from app.models.job import Job
from fastapi import HTTPException
def get_alljobs(db):
  jobs = db.query(Job).all()
  if not jobs:
    raise HTTPException(
      status_code = 404,
      detail = "Job Not Found"
    )
  return jobs
  
  
def createthumbnails(jobs,db):
  print("Jobs:",jobs)
  for job in jobs:
    newJob = Job(
      title = job["title"],
      company_name = job["company_name"],
      url = job["url"],
      category = job["category"],
      tags = job["tags"],
      job_type = job["job_type"],
      publication_date = job["publication_date"],
      candidate_required_location = job["candidate_required_location"],
      salary = job["salary"],
      description = job["description"]
    )
    db.add(newJob)
  db.commit()
  return{
    "message":"Scrapped Thumbnails saved successfully"
  }
  
def showdetails(jobId,db):
  isexists = db.query(Job).filter(Job.id == jobId).first()
  if not isexists:
    raise HTTPException(
      status_code = 404,
      detail = "Job not found!"
    )
  return isexists