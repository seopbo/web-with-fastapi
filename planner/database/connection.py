from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(
	database_connection_string, # 데이터베이스 uri을 인수로 사용한다.
	echo=True, # True로 설정하면 실행된 SQL 명령을 출력한다.
    connect_args=connect_args
)

def conn():
	# 데이터베이스 뿐만 아니라 테이블도 생성, 데이터 베이스 연결파일(connection.py)에서 테이블
	# 파일을 임포트해야함.
	SQLModel.metadata.create_all(engine_url)


def get_session():
	with Session(engine_url) as session:
		yield session
