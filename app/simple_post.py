import requests
import json


url = "http://localhost:8000/process/"  # POSTリクエストを送信するエンドポイントのURL

data = {
    "user_id": "example_user", # ユーザID
    "query"  : "example_query" # ユーザが投げるクエリ(=プロンプト)
}

response = requests.post(url, json=data) # エンドポイントにクエリを投げる

# レスポンスの内容を表示
print(response.json())
