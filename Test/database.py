from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:3306@localhost:3306/student_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()