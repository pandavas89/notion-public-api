"""
Append API Core Logic

notion_client를 이용해 지정된 page에 문구를 삽입합니다.
"""
from notion_client import Client
from notion_client.errors import APIResponseError

def append_block(access_token: str, page_id: str, text: str) -> bool:
    """access_token, page_id, text를 입력받아 지정된 페이지에 텍스트를 삽입합니다"""
    try:
        client = Client(auth=access_token)
        client.blocks.children.append(block_id=page_id, children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": text,
                            }
                        }
                    ]
                }
            }
        ])
        return True
        
    except APIResponseError as e:
        print(f"노션 API 에러: {e.code} - {e.message}")
        return False
    
    except Exception as e:
        print(f"노션 API 에러: {e}")
        return False
