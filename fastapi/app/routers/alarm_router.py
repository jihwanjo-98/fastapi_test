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
    prefix="/alarm",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def alarm_info(db: Session = Depends(get_db)):
    alarm_info={}
    now_value = db.query(Classifier).join(Regions, Classifier.obs_id==Regions.obs_id).filter(Regions.reg2=='강남구').order_by(desc(Classifier.date)).first()
    if now_value:
        alarm_info['now_value']=json.loads(Classifierschema.from_orm(now_value).model_dump_json())
    else:
        raise HTTPException(status_code=404, detail="info not found")
    if alarm_info:
        return JSONResponse(alarm_info)
    else:
        raise HTTPException(status_code=404, detail="info not found")

