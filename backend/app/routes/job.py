from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.services.job import get_alljobs,createthumbnails,showdetails
from app.database.database import get_db
from app.scrapper.jobscrapper import scrape_remotive_jobs

router = APIRouter(
  prefix = "/api/job",
  tags = ["Jobs"]
)

@router.post("/createthumbnails")
def create_thumb(db:Session = Depends(get_db)):
  jobs = scrape_remotive_jobs();
  return createthumbnails(jobs,db);

@router.get("/all")
def getall(db:Session = Depends(get_db)):
  return get_alljobs(db) 

@router.get("/job-detail/{jobId}")
def getdetails(jobId:int,db:Session = Depends(get_db)):
  return showdetails(jobId,db)