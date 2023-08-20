from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Regions, Classifier, Damage, Weather

router = APIRouter(
    prefix="/main",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def main_info(db: Session = Depends(get_db)):
    main_info=[]
    class_latest = db.query(Classifier).order_by(Classifier.class_id.desc()).first()
    if class_latest:
        main_info.append(class_latest)
    weather_latest = db.query(Weather).order_by(Weather.w_id.desc()).first()
    if weather_latest:
        main_info.append(weather_latest)
        
    if main_info:
        return main_info
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
        '''