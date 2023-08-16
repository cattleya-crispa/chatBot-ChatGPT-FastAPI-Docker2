from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print("yattodekita?")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


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
