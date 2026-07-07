from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.database.database import Base,engine
from app.core.logger import logger
from app.routes.job import router as job_router

app = FastAPI()

app.include_router(job_router)

try:
  Base.metadata.create_all(bind = engine)
  logger.info("Database Connected!")
except Exception as e:
  print("Database Connection Failed")
  logger.error("Database Connection Failed")
  print(e)

@app.get("/")
def home():
  return{
    "message":"Welcome to job portal"
  }