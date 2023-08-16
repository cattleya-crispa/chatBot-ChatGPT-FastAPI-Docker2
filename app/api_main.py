from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3
import os

app = FastAPI()

class Input(BaseModel):
    user_id: str
    query: str

class Output(BaseModel):
    user_id: str
    query: str
    output: str

# データベースファイルのパス
DB_PATH = 'chat_history.db' # データベース名をchat_historyへ変更


#################################################
############## ↓ChatGPTの処理↓ ###################
#################################################
def chatgpt(query):
    # chatGPTを使って回答を生成するための処理
    print("chat-gpt inquiry start")
    if not query:
        # クエリが空だった時は、NULLを文字列として返す
        print("query was empty")
        return "NULL"
    else:
        # クエリに入力されているときは、ChatGPTで返答を作る
        import openai
        openai.api_key = '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'
        print("chat-gpt awaiting response........")
        response=openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
          messages = [{"role": "user", "content": query}]
        )

        return response['choices'][0]['message']['content']


#################################################
############## ↓ここからメインの処理↓ #################
#################################################
@app.post("/process/")
def main(input_data: Input):
    # 入力データを取得
    user_id = input_data.user_id
    query   = input_data.query


    # 文字列の加工処理
    processed_text = chatgpt(query)


    # データベースの存在を判定
    if os.path.exists(DB_PATH):
		# データベースが存在する場合
        conn   = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    else:
        # データベースが存在しない場合、新しく作成する
        conn   = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
	    
	    # テーブルの作成
        cursor.execute('''CREATE TABLE data
                      (USER_ID TEXT, QUERY TEXT, OUTPUT TEXT)''')

	# データの挿入
    cursor.execute("INSERT INTO data VALUES (?, ?, ?)" ,(user_id, query, processed_text))

	# 変更を確定させる
    conn.commit()

	# データベース接続を閉じる
    conn.close()

    # 処理結果と入力データをまとめて返す
    output_data = Output(user_id=user_id, query=query, output=processed_text)
    return output_data


# 参考サイト　chatGPT
# https://qiita.com/KENTAROSZK/items/540b8c287a2bb31ed4ac
# 参考サイト docker上でfastAPI
# 
# 参考サイト docker構築
# https://qiita.com/Yu_Mochi/items/4fb5b87acdb3003e68db
# https://zenn.dev/satonopan/articles/a3eb04bc94a89d
# 実行方法
# uvicorn main:app --reload --port=8081 --host=0.0.0.0
# python3 -m flask run -p 80 -h 0.0.0.0
# uvicorn api_simple_post:app --reload
# python simple_post.py
# uvicorn api_post_database:app --reload
# 
# chat GPT secret key
# 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