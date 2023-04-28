from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates/")

@todo_router.post("/todo", status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)) -> dict:
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse(name="todo.html", context={"request": request, "todos": todo_list})

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos(request: Request) -> dict:
    return templates.TemplateResponse(name="todo.html", context={"request": request, "todos": todo_list})

 # 경로 매개변수 추가, 경로 매개변수는 리소스를 식별하기위해 API 라우팅에 사용됨.
 # Path 클래스는 라우트 함수에 있는 다른 인수와 경로 매개변수를 구분하는 역할로 사용된다. Path 클래스는 스웨거, ReDoc 등으로 OpenAPI 기반 문서를 자동 생성할 때 라우트 관련 정보를 함께 문서화하도록 도움.
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(name="todo.html", context={"request": request, "todo": todo})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exists")

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
        for todo in todo_list:
            if todo.id == todo_id:
                todo.item = todo_data.item
                return {
                    "message": "Todo updated successfully."
                }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exists")

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exists")

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }
