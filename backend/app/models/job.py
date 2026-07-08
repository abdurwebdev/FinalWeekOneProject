from app.database.database import Base
from sqlalchemy import Column,Integer,String,ARRAY,Text
from pydantic import BaseModel,ConfigDict
from typing import Optional,List

class Job(Base):
  __tablename__ = "jobies"
  id = Column(Integer,primary_key = True,index = True)
  title = Column(String)
  url = Column(String,unique = True,nullable = False)
  company_name = Column(String)
  company_logo = Column(String)
  category = Column(String)
  tags = Column(ARRAY(String))
  job_type = Column(String)
  publication_date = Column(String)
  salary = Column(String)
  candidate_required_location = Column(String)
  description = Column(Text,nullable = True)
  source = Column(String)

class JobUIOverviewSchema(BaseModel):
  model_config = ConfigDict(from_attributes = True)
  id:int
  title:str
  url:str
  company_name:str
  company_logo:Optional[str] = None
  category:str
  tags:List[str]
  job_type:str
  publication_date:str
  salary:str
  candidate_required_location:str
  source:str
  
class JobDetailOverview(JobUIOverviewSchema):
  description:Optional[str] = None
  