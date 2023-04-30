from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"]
)
users = {} # 애플리케이션 내장 데이터베이스

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with suplied username exists"
        )
    users[data.email] = data
    return {
        "message": "User successfully registered!"
    }

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    # 애플리케이션 내장 데이터베이스를 독립된 데이터 베이스를 옮기는 과정을 다룰 때, 암호화를 사용한 패스워드 저장방식으로 갈음할 예정임.
    # 아래와 같이 패스워드를 암호화하지않고 데이터베이스에 일반 텍스트로 저장하는 것은 잘못된 방식임.
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )
    return {
        "message": "User signed in successfully."
    }
