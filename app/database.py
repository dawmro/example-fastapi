from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from time import time
#import psycopg2
#from psycopg2.extras import RealDictCursor
from .config import settings


# SQLALCHEMY_DATABASE_URL = settings.database_hostname
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = "postgresql://qrv@/var/run/postgresql/fastapi"
# sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "var/run/postgresql/fastapi" does not exist
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}, echo=True)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='/var/run/postgresql', database='fastapi', user='qrv', password='', cursor_factory=RealDictCursor)
#         print("Connection to Database successful")
#         cursor = conn.cursor()
#         break
#     except Exception as error:
        
#         print(f"Unable to connect to database")
#         print("Error: ", error)
#         time.sleep(5)