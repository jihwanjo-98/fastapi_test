from typing import Union, Optional
from pydantic import BaseModel,ConfigDict
from datetime import datetime,time,date

class Regionsschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    obs_id: int
    reg1: str
    reg2: str
    lat: float
    lon: float
    reg_code: str
    
class My_regionsschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    inter_key: int
    name: str
    feature: str
    obs_id: int

class Classifierschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    disaster: str
    value: int
    date: date
    time: time
    dt : str
    obs_id: int
    inter_key: int

    
class Damageschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    d_id: int
    disaster: str
    date: str
    summary:str
    damage_class: int
    obs_id: int
    inter_key: int

class Rainschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    obs_id: int
    date: date
    time: time
    before1: float
    before2: float
    before3: float
    after1 : float
    after2 : float
    after3 : float

class Hotschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    obs_id: int
    date: date
    time: time
    value1: float
    value2: float
    value3: float
    target: str

class Actionsschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    disaster: str
    damage_class: int
    action: str

class TempRegionschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    name : str