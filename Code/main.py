from fastapi import FastAPI
from Modules.CreditCard import CreditCard
from Modules.Rating import Rating
from Modules.Book import Book
from Modules.Branch import Branch
from Modules.UserAccount import *
from datetime import datetime
from Modules.dto import CreditCards, BranchModel

class BranchModel():
        branch_name = str
        open_time = datetime
        location = str
        tel = str
        line_id = str
        facebook_id = str
        product_in_stock = str

# class Ratings(BaseModel):
#     book : Book
#     book_rating : int
#     book_comment : str
# class Books(BaseModel):

list_credit_card = []
list_branch = []

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

# how to select object to modify itself
@app.put("/creditCard/")
async def modify_credit_card(credit_card : CreditCards):
    pookan_card.modify_credit_card_info(credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return pookan_card.__dict__

# @app.put("/branch/")
# async def modify_branch(branch : BranchModel):
#     rangsit.modify_branch(branch.branch_name, branch.open_time, branch.location, branch.tel, branch.line_id, branch.facebook_id)

