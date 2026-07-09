import requests
from requests.exceptions import (ConnectTimeout,ReadTimeout,Timeout)
from app.core.logger import logger

def get_jobs_from_remotive():
  try:
    response = requests.get("https://remotive.com/api/remote-jobs",timeout=(3.05,10))
  except ConnectTimeout:
    logger.error("Couldn't connect to Server.")
  except ReadTimeout:
    logger.error("Server conncted but took too long to read data.")
  except Timeout:
    logger.error("Timeout occured.")
  return response.json()