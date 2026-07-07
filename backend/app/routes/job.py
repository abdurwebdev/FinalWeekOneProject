from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.services.job import get_alljobs,createthumbnails
from app.database.database import get_db
from app.scrapper.jobscrapper import scrappedjobs

router = APIRouter(
  prefix = "/api/job",
  tags = ["Jobs"]
)

@router.post("/createthumbnails")
def create_thumb(db:Session = Depends(get_db)):
  jobs = scrappedjobs();
  return createthumbnails(jobs,db);

@router.get("/all")
def getall(db:Session = Depends(get_db)):
  return get_alljobs(db) 