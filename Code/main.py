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
all_branch = BranchList()

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

bangkok = Branch("Bangkok",
                 "6.00 - 22.00",
                 "Bangkok",
                 "0864615559",
                 "bookshop.bangkok",
                 "bangkok_bookshop",
                 [])
all_branch.add_branch(rangsit)

def find_branch_list(name):
    for i in all_branch.list_of_branch:
        if name == i._branch_name:
            return i

pookantong_rating1 = Rating(pookantong_book1, 10, "Bad ending, I don't like it")

@app.get("/")
async def home():
    return {"Welcome to BookShop"}

@app.post("/addCreditCard/")
async def add_credit_card(credit_card : CreditCardDTO):
    list_credit_card.append(CreditCard(credit_card.card_num, credit_card.expire_date, credit_card.cvc))
    return list_credit_card

# loop to get credit card object
@app.put("/modifyCreditCard/")
async def modify_credit_card(credit_card : CreditCardDTO):
    pookan_card.modify_credit_card_info(credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return pookan_card

@app.post("/addbranch")
async def add_branch(data:AddBranchDTO):
    all_branch.add_branch(Branch(data.branch_name,
                data.open_time,
                data.location,
                data.tel,
                data.line_id,
                data.facebook_id))
    return all_branch.list_of_branch

@app.put("/branch/{branch_name}")
async def modify_branch(branch : ModifyBranchDTO, branch_name):
    find_branch = find_branch_list(branch_name)
    find_branch.modify_branch(branch.branch_name, branch.open_time, branch.location, branch.tel, branch.line_id, branch.facebook_id,[],[])
    return find_branch

@app.post("/addEvent/")
async def add_event(data : EventDTO):
    list_event.append(EventDiscount(data.event_name, data.event_start, data.event_end, data.discounted_percentage))
    return list_event

