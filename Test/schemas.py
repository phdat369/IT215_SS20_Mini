from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Any, Optional

class CreateStudent(BaseModel):
    student_code: str = Field(min_length=3,max_length=20)
    full_name: str = Field(min_length=2,max_length=100)
    email: EmailStr = Field(min_length=1)
    class_id: int = Field(ge=1)

class ClassroomResponse(BaseModel):
    id: int
    class_code: str
    class_name: str
    model_config = ConfigDict(from_attributes=True)
class StudentResponse(BaseModel):
    id: int
    student_code: str
    full_name: str
    email: EmailStr
    classroom: ClassroomResponse
    model_config = ConfigDict(from_attributes=True)
class BaseResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any] = None
    erro: Optional[str] = None