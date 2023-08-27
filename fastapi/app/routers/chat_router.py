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
    prefix="/chat",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/actions/")
async def action_info(db: Session = Depends(get_db)):
    action_info={}
    action = db.query(Actions).filter_by(damage_class=3, disaster="호우").first()    
    if action:
        action_info['action_info'] = json.loads(Actionsschema.from_orm(action).model_dump_json())
    else:
        raise HTTPException(status_code=404, detail="info not found")
    
    if action_info:
        return JSONResponse(action_info)
    else:
        raise HTTPException(status_code=404, detail="info not found")
    
@router.get("/damages/")
async def damage_info(db: Session = Depends(get_db)):
    damage_info={}
    
    damage =db.query(Damage).join(Regions, Damage.obs_id==Regions.obs_id).filter(Regions.reg2=='강남구').order_by(desc(Damage.date)).first()
    if damage:
        damage_info['damage_info'] = json.loads(Damageschema.from_orm(damage).model_dump_json())
    else:
        raise HTTPException(status_code=404, detail="info not found")
    
    if damage_info:
        return JSONResponse(damage_info)
    else:
        raise HTTPException(status_code=404, detail="info not found")

