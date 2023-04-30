from fastapi import FastAPI
from routes.users import user_router
import uvicorn

app = FastAPI()
# 라우트 등록
app.include_router(user_router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
