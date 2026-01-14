from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_url = "mysql+pymysql://root:1234@localhost:3306/fastapi_db"
engine = create_engine(db_url,echo=True)
sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()
