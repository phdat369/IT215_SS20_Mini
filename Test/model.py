from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class ClassRoomModel(Base):
    __tablename_ = "classrooms"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    class_code = Column(String(10),nullable=False,unique=True)
    class_name = Column(String(50),nullable=False,unique=True)
    class_room = relationship("StudentModel",back_populates="students")
class StudentModel(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    student_code = Column(String(10),nullable=False,unique=True)
    full_name = Column(String(50),nullable=False)
    email = Column(String(50),nullable=False,unique=True)
    class_id = Column(Integer,ForeignKey("classrooms.id"),nullable=False)
    students = relationship("ClassRoomModel",back_populates="class_roome")
