"""
FastAPI Wrapper, 코어 함수들을 로컬 환경에서 실행할 수 있도록 제공합니다
"""
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

public_api_router = APIRouter(prefix="/public-api")

@public_api_router.get("/register")
def register(request: Request):
    return {"message": "Registration successful"}

@public_api_router.post("/quote")
def quote():
    return {"message": "Quote retrieved"}

app.include_router(daily_quote_router)