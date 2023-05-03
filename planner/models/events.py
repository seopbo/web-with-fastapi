from sqlmodel import JSON, SQLModel, Field, Column
from typing import List, Optional

class Event(SQLModel, table=True): # 이벤트 모델
    id: int = Field(default=None, primary_key=True) # 자동 생성되는 고유 식별자
    title: str # 이벤트 타이틀
    image: str # 이벤트 이미지 배너의 링크
    description: str # 이벤트 설명
    tags: List[str] = Field(sa_column=Column(JSON))# 그룹화를 위한 이벤트 태그
    location: str # 이벤트 위치
    
    class Config: # 문서화시 샘플 데이터를 보여주기위한 용도로 추가, API를 통해 신규 이벤트를 생성할 때 참고가능
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gitfs!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

# UPDATE 처리의 바디 유형으로 사용할 SQLModel 클래스를 추가한다.
class EventUpdate(SQLModel):
    title: Optional[str]
    image : Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }   
        }