from fastapi import FastAPI
from Modules.Catalog import Catalog
app = FastAPI()

batalog = Catalog()

def event_dis():
    for i in batalog.list_all_of_book:
    if i._name in [x._name for x in event.list_of_book]:
        event.apply_discount(i)

@app.get("/catalog")
async def show_items(batalog):
    