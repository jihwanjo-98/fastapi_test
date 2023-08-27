from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Regions, Classifier, Damage, Weather


'''  ------------------------------------------  # 폐기  ---------------------
router = APIRouter(
    prefix="/weather",   
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def weather_list(db: Session = Depends(get_db)):
    damage_latest = db.query(Weather).order_by(Weather.d_id.desc()).first()
    if damage_latest:
        return damage_latest
    else:
        raise HTTPException(status_code=404, detail="damage not found")

'''