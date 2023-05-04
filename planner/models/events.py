from beanie import Document
from typing import Optional, List
from pydantic import BaseModel

class Event(Document):
    title: str # 이벤트 타이틀
    image: str # 이벤트 이미지 배너의 링크
    description: str # 이벤트 설명
    tags: List[str]# 그룹화를 위한 이벤트 태그
    location: str # 이벤트 위치
    
    class Config: # 문서화시 샘플 데이터를 보여주기위한 용도로 추가, API를 통해 신규 이벤트를 생성할 때 참고가능
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gitfs!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

    class Settings:
        name = "events"

# UPDATE 처리를 위한 pydantic 모델을 추가함.
class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI BookLaunch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
