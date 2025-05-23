"""
Register API Core Logic

Notion Public API를 이용해 사용자 Access Token을 발급받습니다
"""
import requests
import os

NOTION_CLIENT_ID = os.getenv("NOTION_CLIENT_ID")
NOTION_CLIENT_SECRET = os.getenv("NOTION_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

NOTION_OAUTH_URL = "https://api.notion.com/v1/oauth/token"

def get_access_token(code: str) -> str:
    """OAuth 콜백 함수로서 호출되어 인증 결과를 ACCESS_TOKEN으로 전환합니다"""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    auth = (NOTION_CLIENT_ID, NOTION_CLIENT_SECRET)

    res = requests.post(NOTION_OAUTH_URL, data=data, auth=(NOTION_CLIENT_ID, NOTION_CLIENT_SECRET))
    if res.status_code != 200:
        return ""
    token_data = res.json()
    access_token = token_data["access_token"]

    return access_token