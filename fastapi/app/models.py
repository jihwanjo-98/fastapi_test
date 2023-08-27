from sqlalchemy import Column, Integer, String, Float, DateTime, Date, Time, ForeignKey, Text,PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from database import Base


class Regions(Base):
    __tablename__ = 'regions'
    obs_id = Column(Integer, primary_key=True)
    reg1 = Column(String(100))
    reg2 = Column(String(50))
    lat = Column(Float)
    lon = Column(Float)
    reg_code = Column(String(30))

    # Relationships
    region_to_damage = relationship("Damage", back_populates="damage_to_region")
    region_to_classifier = relationship("Classifier", back_populates="classifier_to_region")
    region_to_rain = relationship("Rain", back_populates="rain_to_region")
    region_to_hot = relationship("Hot", back_populates="hot_to_region")
    region_to_criterion = relationship("Criterion", back_populates="criterion_to_region")
    region_to_my_region = relationship("My_regions", back_populates="my_region_to_region")


class My_regions(Base):
    __tablename__ = 'my_regions'
    inter_key = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    feature = Column(String(100))
    obs_id = Column(Integer, ForeignKey('regions.obs_id'))
    
    my_region_to_region = relationship("Regions",back_populates="region_to_my_region")
    my_region_to_classifier = relationship("Classifier", back_populates="classifier_to_my_region")
    my_region_to_damage = relationship("Damage", back_populates="damage_to_my_region")
    
class Damage(Base):
    __tablename__ = 'damage'
    d_id = Column(Integer, primary_key=True, autoincrement=True)
    disaster = Column(String(20))
    date = Column(String(30))
    summary=Column(String(500))
    damage_class = Column(Integer)
    obs_id = Column(Integer, ForeignKey('regions.obs_id'))
    inter_key = Column(Integer, ForeignKey('my_regions.inter_key'))

    # Relationships
    damage_to_region = relationship("Regions", back_populates="region_to_damage")
    damage_to_my_region = relationship("My_regions", back_populates="my_region_to_damage")

class Actions(Base):
    __tablename__ = 'actions'
    disaster = Column(String(20))
    damage_class = Column(Integer)  # If this is a typo, please correct it
    action = Column(Text)
    __table_args__ = (
        PrimaryKeyConstraint('disaster', 'damage_class'),
    )

class Classifier(Base):
    __tablename__ = 'classifier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    disaster = Column(String(20))
    value = Column(Integer)
    date = Column(Date)
    time = Column(Time)
    dt = Column(String(50))
    obs_id = Column(Integer, ForeignKey('regions.obs_id'))
    inter_key = Column(Integer, ForeignKey('my_regions.inter_key'))

    # Relationships
    classifier_to_region = relationship("Regions", back_populates="region_to_classifier")
    classifier_to_my_region = relationship("My_regions", back_populates="my_region_to_classifier")

class Rain(Base):
    __tablename__ = 'rain'
    obs_id = Column(Integer, ForeignKey('regions.obs_id'), primary_key=True, autoincrement=True)
    date = Column(Date)
    time = Column(Time)
    before1 = Column(Float)
    before2 = Column(Float)
    before3 = Column(Float)
    after1= Column(Float)
    after2= Column(Float)
    after3= Column(Float)
    # Relationships
    rain_to_region = relationship("Regions", back_populates="region_to_rain")

class Hot(Base):
    __tablename__ = 'hot'
    obs_id = Column(Integer, ForeignKey('regions.obs_id'), primary_key=True, autoincrement=True)
    date = Column(Date)
    time = Column(Time)
    value1 = Column(Float)
    value2 = Column(Float)
    value3 = Column(Float)
    target = Column(String(100))

    # Relationships
    hot_to_region = relationship("Regions", back_populates="region_to_hot")

class Criterion(Base):
    __tablename__ = 'criterion'
    obs_id = Column(Integer, ForeignKey('regions.obs_id'), primary_key=True)
    grade1 = Column(Float)
    grade2 = Column(Float)
    grade3 = Column(Float)

    # Relationships
    criterion_to_region = relationship("Regions", back_populates="region_to_criterion")


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