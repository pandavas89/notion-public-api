"""
FastAPI Wrapper, 코어 함수들을 로컬 환경에서 실행할 수 있도록 제공합니다
"""
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse

from register.register import get_access_token

app = FastAPI()

public_api_router = APIRouter(prefix="/public-api")

@public_api_router.get("/register")
def register(request: Request):
    code = request.query_params.get("code")
    access_token = get_access_token(code)
    if access_token:
        print(access_token) # 배포 시 ACCESS TOKEN 저장 코드로 대체
        return {"message": "퍼블릭 API 등록 성공"}
    return {"message": "퍼블릭 API 등록 실패"}

app.include_router(public_api_router)