# notion-public-api
Notion public API 사용방법 예제입니다.

## 개발 환경
- python 기반 FastAPI 애플리케이션
- 로컬 배포: `localhost:8000`에서 실행

## 서비스 구성
### 1. Register
사용자 인증을 위해 Notion OAuth 콜백 API를 제공하고, 수신한 code를 기반으로 ACCESS TOKEN을 취득합니다.  
예제이므로, ACCESS TOKEN 취득 이후의 저장은 다루지 않습니다.

> Endpoint: GET `/public-api/register`

### 2. Append
획득한 ACCESS TOKEN을 기반으로 연동이 추가된 페이지에 대한 수정을 진행합니다.

> Endpoint: POST `/public-api/append`

