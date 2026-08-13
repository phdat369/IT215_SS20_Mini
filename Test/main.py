from model import StudentModel,ClassRoomModel
from database import engine,Base,get_db
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/students")
def get_student(db: Session = Depends(get_db)):
    