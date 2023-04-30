from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(BaseModel): # 사용자 모델
    email: EmailStr # 사용자 이메일
    password: str # 사용자 패스워드
    events: Optional[List[Event]] # 해당 사용자가 생성한 이벤트, 처음에는 비어있음.
    
    class Config: # 샘플 데이터
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": []
            }
        }

class UserSignIn(BaseModel): # 사용자 로그인모델
    email: EmailStr
    password: str
    
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }
