from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta,declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from sqlalchemy import MetaData

from dotenv import load_dotenv
import os

# .env 파일을 로드
load_dotenv()

# 환경 변수에 접근
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')

metadata = MetaData()

#SQLALCHEMY_DATABASE_URL = "sqlite:///./disaster_app.db"
#DATABASE_URL = "mysql://username:password@localhost/dbname"

DATABASE_URL = f"mysql+pymysql://jihwan:{MYSQL_ROOT_PASSWORD}@{MYSQL_HOST}:3306/disaster_db"
database = Database(DATABASE_URL)
Base = declarative_base(metadata=metadata)

engine = create_engine(
    DATABASE_URL
    #, connect_args={"check_same_thread": False}   sqlite일때만 필요함
)
#Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)