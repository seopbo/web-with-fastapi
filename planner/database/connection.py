from typing import Any, List, Optional

from beanie import init_beanie, PydanticObjectId
from models.events import Event
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    # 데이터베이스를 초기화하는 메서드
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL) # 데이터베이스 URL은 Config 서브클래스에 정의된 환경 파일(env_file)에서 읽어온다.
        await init_beanie(database=client.get_default_database(), document_models=[Event, User]) # 데이터베이스 클라이언트를 설정함.

    class Config:
        env_file = ".env"


class Database:
    def __init__(self, model): # 데이터베이스 초기화 중에 사용되는 모델은 Event 또는 User 문서의 모델
        self.model = model

    # 레코드 하나를 데이터베이스 컬렉션에 추가한다.
    # 문서의 인스턴스를 받아서 데이터베이스 인스턴스에 전달함.
    async def save(self, document) -> None:
        await document.create()
        return

    # id를 인수로 받아서 컬렉션에서 일치하는 레코드를 조회
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    # 컬렉션에 있는 모든 레코드를 조회
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()

        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True