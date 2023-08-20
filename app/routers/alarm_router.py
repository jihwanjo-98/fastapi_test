from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Regions, Classifier, Damage, Weather

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
    alarm_info=[]
    class_latest = db.query(Classifier).order_by(Classifier.class_id.desc()).first()
    if class_latest:
        alarm_info.append(class_latest)
    damage_latest = db.query(Weather).order_by(Weather.w_id.desc()).first()
    if damage_latest:
        alarm_info.append(damage_latest)
        
    if alarm_info:
        return alarm_info
    else:
        raise HTTPException(status_code=404, detail="info not found")

