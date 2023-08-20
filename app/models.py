from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIME,PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from database import Base


from sqlalchemy import Column, Integer, String, Date, Float, TIMESTAMP, Text
from sqlalchemy.ext.declarative import declarative_base


class Weather(Base):
    __tablename__ = 'weather'
    
    w_id = Column(Integer, primary_key=True, index=True)
    disaster = Column(String(20))
    date = Column(Date)
    time = Column(TIME)
    value = Column(Float)
    region_id = Column(Integer, ForeignKey("regions.region_id"))
    regions = relationship("Regions", backref="weathers")


class Damage(Base):
    __tablename__ = 'damage'
    
    d_id = Column(Integer, primary_key=True, index=True)
    disaster = Column(String(20))
    date = Column(Date)
    d_value = Column(Integer)
    d_human = Column(Integer)
    status = Column(String(20))
    damage_class = Column(Integer)
    region_id = Column(Integer, ForeignKey("regions.region_id"))
    regions = relationship("Regions", backref="damages")



class Actions(Base):
    __tablename__ = 'actions'
    
    disaster = Column(String(20))
    damage_class = Column(Integer)
    action = Column(Text)
    __table_args__ = (
        PrimaryKeyConstraint('disaster', 'damage_class'),
    )

class Classifier(Base):
    __tablename__ = 'classifier'
    
    class_id = Column(Integer, primary_key=True, index=True)
    disaster = Column(String(20))
    value = Column(Float)
    date = Column(Date)
    time = Column(TIME)
    region_id = Column(Integer, ForeignKey("regions.region_id"))
    regions = relationship("Regions", backref="classes")

class Regions(Base):
    __tablename__ = 'regions'
    
    region_id = Column(Integer, primary_key=True, index=True)
    region_name = Column(String(20))

'''
from models import Regions, Classifier, Damage, Weather
region = Regions(region_id=1,region_name='보라매')

from database import SessionLocal
db = SessionLocal()
db.add(region)
db.commit()
   


from models import Regions, Classifier, Damage, Weather
from database import SessionLocal
from datetime import datetime, time, date
db = SessionLocal()
r = db.query(Regions).get(1)
damage = Damage(regions=r, class_id=1, disaster="호우",value=100
,date=date(2023, 8, 20),time=time.fromisoformat("14:52:00"))
db.add(predict)
db.commit() 
'''