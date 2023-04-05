from fastapi import FastAPI
from Modules.CreditCard import CreditCard
from Modules.Rating import Rating
from Modules.Book import Book
from Modules.Branch import Branch
from Modules.BranchList import BranchList
from Modules.UserAccount import *
from Modules.EventDiscount import EventDiscount
from datetime import datetime
from Modules.dto import *
from pydantic import BaseModel

list_credit_card = []
list_event = []
list_branch = BranchList()

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
async def add_credit_card(credit_card : CreditCardDTO):
    list_credit_card.append(CreditCard(credit_card.card_num, credit_card.expire_date, credit_card.cvc))
    return list_credit_card

# loop to get credit card object
@app.put("/creditCard/")
async def modify_credit_card(credit_card : CreditCardDTO):
    pookan_card.modify_credit_card_info(credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return pookan_card

@app.put("/branch/")
# loop to get branch object
async def modify_branch(branch : ModifyBranchDTO):
    rangsit.modify_branch(branch.branch_name, branch.open_time, branch.location, branch.tel, branch.line_id, branch.facebook_id,[],[])
    return rangsit

@app.post("/event/")
async def add_event(data : EventDTO):
    list_event.append(EventDiscount(data.event_name, data.event_start, data.event_end, data.discounted_percentage))
    return list_event

