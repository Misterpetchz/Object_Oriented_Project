from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello world!"}
@app.get("/hi")
async def hi(name:str, reply: Optional[str] = None):
    return {"Hello":name, "reply = " : reply}

# @app.post('/book/')
# async def add_rating(rating : Ratings):
#     pookantong_book1.add_rating(rating.book_rating, rating.book_comment)
#     return pookantong_book1._rating.__dict_