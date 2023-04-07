from fastapi import FastAPI, BackgroundTasks
from Modules.CreditCard import CreditCard
from Modules.Rating import Rating
from Modules.Book import Book
from Modules.Branch import Branch
from Modules.BranchList import BranchList
from Modules.UserAccount import *
from Modules.EventDiscount import EventDiscount
from Modules.Payment import *
from datetime import datetime
from Modules.dto import *
from fastapi.responses import FileResponse, HTMLResponse
import time

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

moon_branch = Branch('Moon',
                     '23:00 - 23:59',
                     'Moon',
                     '0995471568',
                     'bookshop.moon',
                     'moon_bookshop'
                     ,[])

# all_branch.add_branch(rangsit)
# pookantong_rating1 = Rating(pookantong_book1, 10, "Bad ending, I don't like it")

@app.get("/")
async def home():
    return {"Welcome to BookShop"}


@app.get("/GetCreditCard/")
async def get_credit_card():
    return list_credit_card

@app.post("/AddCreditCard/")
# user make this
async def add_credit_card(credit_card : CreditCardDTO):
    # use method in class
    list_credit_card.append(CreditCard(credit_card.card_num, credit_card.expire_date, credit_card.cvc))
    return {"Add CreditCard Success"}

# edit this
@app.put("/ModifyCreditCard/")
async def modify_credit_card(credit_card : CreditCardDTO):
    pookan_card.modify_credit_card_info(credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return pookan_card

@app.get("/GetAllBranch/")
async def get_branch():
    return {all_branch}

@app.post("/AddBranch")
async def add_branch(data:AddBranchDTO):
    all_branch.add_branch(Branch(data.branch_name,
                data.open_time,
                data.location,
                data.tel,
                data.line_id,
                data.facebook_id,
                []))
    #return all_branch.list_of_branch
    return {"Add Branch Success"}

@app.put("/ModifyBranch/{branch_name}")
async def modify_branch(data : ModifyBranchDTO, branch_name):
    select_branch = all_branch.select_branch(branch_name)
    select_branch.modify_branch(data.branch_name, 
                                data.open_time, 
                                data.location, 
                                data.tel, 
                                data.line_id, 
                                data.facebook_id, 
                                data.add_book, 
                                data.remove_book)
    return {"Modify Success"}

@app.get("/GetAllEvent/")
async def get_event():
    return list_event

@app.post("/AddEvent/")
async def add_event(data : EventDTO):
    list_event.append(EventDiscount(data.event_name, 
                                    data.event_start, 
                                    data.event_end, 
                                    data.discounted_percentage))
    return {"Add Event Success"}

# we dont place to collect class bookshop
@app.put("/ModifyEvent/{event_name}")
async def modify_event(data : ModifyEventDTO, event_name):
    # loop check in bigger class
    for i in list_event:
        if event_name == i.event_name:
            select_event = i
    select_event.modify_event(data.event_name,
                              data.event_start,
                              data.event_end,
                              data.discounted_percentage)
    return {"Modify Success"}

@app.get("/QrPayment")
async def check_payment():
    time.sleep(3)
    return {"Transaction Complete!"}

@app.post("/QrPayment/")
async def generate_qr(data : QrCodeDTO, background_tasks : BackgroundTasks):
    transactions = ViaQrCode(data.amount, data.date)
    transactions.generate_qr_code()
    background_tasks.add_task(check_payment)
    return FileResponse("../qrcode-0890767442.png")