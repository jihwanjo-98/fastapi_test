from fastapi import FastAPI
#from models import HumanToMemory, Human, Memory
#from sqlalchemy.sql import select
from starlette.middleware.cors import CORSMiddleware

from routers import main_router
from routers import alarm_router
#from routers import weather_router

from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

#CORS 예외 URL을 등록
origins = [
    "http://127.0.0.1:8000",    # savelte 실행했을때, 열리는 포트번호 입력 "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/items/")
async def create_item(item: Item):
    return item

app.include_router(main_router.router)
app.include_router(alarm_router.router)
#app.include_router(weather_router.router)