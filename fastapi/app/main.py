from fastapi import FastAPI
#from models import HumanToMemory, Human, Memory
#from sqlalchemy.sql import select
from starlette.middleware.cors import CORSMiddleware

from routers import main_router,alarm_router,chat_router
from database import database
#from routers import weather_router

from pydantic import BaseModel
from typing import Union


app = FastAPI()

#CORS 예외 URL을 등록
origins = [
    "http://127.0.0.1:8000",    # aws 인바운드 규칙에 설정한 TCP 및 포트번호 입력 "http://0.0.0.0:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',    # 사용자 정의 orgins가 아니라 전부 허용하는 것으로 설정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
'''
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
'''

app.include_router(main_router.router)
app.include_router(alarm_router.router)
app.include_router(chat_router.router)
#app.include_router(weather_router.router)