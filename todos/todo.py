from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }

 # 경로 매개변수 추가, 경로 매개변수는 리소스를 식별하기위해 API 라우팅에 사용됨.
 # Path 클래스는 라우트 함수에 있는 다른 인수와 경로 매개변수를 구분하는 역할로 사용된다. Path 클래스는 스웨거, ReDoc 등으로 OpenAPI 기반 문서를 자동 생성할 때 라우트 관련 정보를 함께 문서화하도록 도움.
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    return {
        "message": "Todo with supplied ID doesn't exists."
    }
