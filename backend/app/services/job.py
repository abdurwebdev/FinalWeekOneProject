from app.models.job import Job
from fastapi import HTTPException
from app.core.logger import logger

def get_alljobs(db):
  jobs = db.query(Job).all()
  if not jobs:
    raise HTTPException(
      status_code = 404,
      detail = "Job Not Found"
    )
  return jobs
  
  
def save_jobs_to_db(jobs,db):
  inserted = 0
  duplicates = 0
  failed = 0
  try:
    logger.info(f"Running {jobs[0].source} Scrapper....")
    logger.info(f"Fetched {len(jobs)} Jobs.....")
    for job in jobs:
      duplicate_job = db.query(Job).filter(Job.url == job.url).first()
      if duplicate_job:
        duplicates+=1
        logger.info(f"Duplicate Job Skipped {job.title}")
        continue
      new_job = Job(
      title = job.title,
      company_name = job.company_name,
      url = job.url,
      category = job.category,
      tags = job.tags,
      job_type = job.job_type,
      publication_date = job.publication_date,
      candidate_required_location = job.candidate_required_location,
      salary = job.salary,
      description = job.description,
      source = job.source
    )
      db.add(new_job)
      inserted+=1
    db.commit()
    logger.info(f"Inserted {inserted} Jobs.....")
    logger.info(f"{jobs[0].source}scrape completed Successfully.")
    return{
    "scrapped":len(jobs),
    "inserted":inserted,
    "duplicates":duplicates,
    "failed":failed,
    "new_jobs":inserted
  }
  except Exception as e:
    failed+=1
    db.rollback();
    logger.exception(f"Error scraping job",e)
    raise;
def showdetails(jobId,db):
  isexists = db.query(Job).filter(Job.id == jobId).first()
  if not isexists:
    raise HTTPException(
      status_code = 404,
      detail = "Job not found!"
    )
  return isexists