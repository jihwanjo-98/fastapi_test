from fastapi import APIRouter,Depends,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import desc, func, and_
from database import SessionLocal
from models import *
from schemas import *

from pydantic import BaseModel, ConfigDict
from typing import Union, Optional
from datetime import datetime,time,date
import json

router = APIRouter(
    prefix="/main",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/now/")
async def now_info(db: Session = Depends(get_db)): #, response_model=schemas.Post
    now_info={}
    now_row = db.query(Classifier).join(Regions, Classifier.obs_id==Regions.obs_id).filter(Regions.reg2=='강남구').order_by(desc(Classifier.date)).first()
    if now_row:
        print(json.loads(Classifierschema.from_orm(now_row).model_dump_json()))
        now_info['now_row']=json.loads(Classifierschema.from_orm(now_row).model_dump_json())
        print(now_info)
    else:
        raise HTTPException(status_code=404, detail="info not found")
    if now_info:
        return now_info
    else:
        raise HTTPException(status_code=404, detail="info not found")
        
@router.get("/interest/")
async def interest_info(db: Session = Depends(get_db)):
    interest_info={}
    
    subquery = (
    db.query(func.max(Classifier.dt).label("max_dt"), My_regions.obs_id)
    .join(Regions, Classifier.obs_id == Regions.obs_id)
    .join(My_regions, Regions.obs_id == My_regions.obs_id)
    .group_by(My_regions.obs_id)
    .subquery()
    )
    
    interest_value = db.query(Classifier).join(Regions,
        Classifier.obs_id == Regions.obs_id).join(My_regions,Regions.obs_id == My_regions.obs_id).join(subquery, 
          (Classifier.dt == subquery.c.max_dt) & 
          (My_regions.obs_id == subquery.c.obs_id)).order_by(desc(Classifier.dt))
    
    if interest_value:
        interest_info['interest_value']=[json.loads(Classifierschema.from_orm(item).model_dump_json()) for item in interest_value]
    if interest_info:
        return interest_info
    else:
        raise HTTPException(status_code=404, detail="info not found")


'''
@router.get("/")
async def weather_list(db: Session = Depends(get_db)):
    damage_latest = db.query(Weather).order_by(Weather.d_id.desc()).first()
    if damage_latest:
        return damage_latest
    else:
        raise HTTPException(status_code=404, detail="damage not found")
        
        
class ClassifierModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    class_id: int
    disaster: str
    value: float
    date: datetime
    time: time
    


class WeatherModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    w_id: int
    disaster : str
    date: datetime
    time : time
    value : float
        '''