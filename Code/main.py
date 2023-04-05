from fastapi import FastAPI
from Modules.CreditCard import CreditCard
from Modules.Rating import Rating
from Modules.Book import Book
from Modules.Branch import Branch
from Modules.BranchList import BranchList
from Modules.UserAccount import *
from datetime import datetime
from Modules.dto import CreditCards
from pydantic import BaseModel

list_credit_card = []
list_branch = BranchList()

class Branchs(BaseModel):
    branch_name : str
    open_time : str
    location : str
    tel : str
    line_id : str
    facebook_id : str

app = FastAPI()
pookan_card = CreditCard("121231232",
                         "15-07-22",
                         "123")
pookantong_book1 = Book(2547,
                       'random.png',
                       'ในคืนที่โหดร้ายพระเอกตายแต่.....',
                       'Pookantong',
                       'Pookantong1',
                       '250 หน้า ปกแข็ง',
                       '8472ae0Kjd7',
                       'BanDao',
                       'yamete!',
                       'critic review',
                       [],
                       'พระเอกตาย',
                       ['comedy','adult','intense','violent','drama','romantic','Yuri','Yaoi','School life'],
                       '18/12/29999',
                       [],
                       999)

pookan_admin555 = Admin('65010895@kmitl.ac.th',
                 'PomyukmeFan55',
                 'Yotsapat',
                 'Male',
                 '0980231172',
                 [],
                 True)

rangsit = Branch('rangsit',
                       '9:00-23:00',
                       'future park rangsit',
                       '0983868365',
                       'bookshop.rangsit',
                       'rangsit_bookshop',
                       [])

pookantong_rating1 = Rating(pookantong_book1, 10, "Bad ending, I don't like it")

@app.get("/")
async def home():
    return {"Welcome to BookShop"}

@app.post("/CreditCard/")
async def add_credit_card(credit_card : CreditCards):
    list_credit_card.append(CreditCard(credit_card.card_num, credit_card.expire_date, credit_card.cvc))
    return list_credit_card

# loop to get credit card object
@app.put("/creditCard/")
async def modify_credit_card(credit_card : CreditCards):
    pookan_card.modify_credit_card_info(credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return pookan_card.__dict__

@app.post("/branch/")
async def add_branch(branch : Branchs):
    pookan_admin555.add_branch(list_branch, branch)
    return list_branch.list_of_branch

@app.put("/branch/")
# loop to get branch object
async def modify_branch(branch : dict):
    branch_name = branch["branch_name"]
    open_time = branch["open_time"]
    location = branch["location"]
    tel = branch["tel"]
    line_id = branch["line_id"]
    facebook_id = branch["facebook_id"]
    rangsit.modify_branch(branch_name, open_time, location, tel, line_id, facebook_id,[],[])
    return rangsit