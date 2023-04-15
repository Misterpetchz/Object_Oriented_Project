from fastapi import FastAPI, Request ,Form,Response
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from Modules.Catalog import Catalog
from Modules.EventDiscount import EventDiscount
from Modules.Book import *
from Modules.UserAccount import *
from Modules.System import *
from Modules.settings import *
from Modules.BranchList import BranchList
from Modules.Branch import Branch
from Modules.Order import Order
from Modules.CreditCard import CreditCard
from Modules.Rating import Rating
from Modules.UserAccount import *
from Modules.dto import *
from Modules.settings import *
from CLassDTO import *
from Modules.EventDiscount import EventDiscount
from Modules.Payment import *
from datetime import datetime
import random
from Modules.dto import *
from Modules.BookShop import BookShop
from fastapi.responses import FileResponse, RedirectResponse
import time
import datetime
import starlette.status as status

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static",
    StaticFiles(directory="static"),
    name="static")

shop = BookShop()
User_DB = []
list_credit_card = []

list_branch = BranchList()
Sys = System()
class Branchs(BaseModel):
    branch_name : str
    open_time : str
    location : str
    tel : str
    line_id : str
    facebook_id : str

pookan_card = CreditCard("121231232",
                         "15-07-22",
                         "123")

nonthaburi1 = Branch("Nonthaburi",
                     "8:30-22:00",
                     "Nonthaburi",
                     "0811111111",
                     "seed_nonthaburi01",
                     "NonthaburiSE-ED",
                     )
shop.add_branch(nonthaburi1)
pookaneiei = Customer("pookan@gmail.com", Sys.get_password_hash("test1"), "pookan", "Male", "0000000000", True, False, "LLL")
Sys.User_DB.append(pookaneiei)
# pookaneiei = Customer('pookantong.p@gmail.com',
#                  'PomyukmeFan555',
#                  'PookanNaja',
#                  'Male',
#                  '0980231173',
#                  [],
#                  '29/7 หมู่2 ตำบลบั้นเด้า อำเภอรถแห่ จังหวัดสก๊อย ประเทศหิวข้าว ดาวSun',
#                  True,
#                  True)

batalog = Catalog()

# Sys.User_DB.append(Customer(input_dict["_email"], input_dict["_password"], input_dict["_full_name"], input_dict["_gender"], input_dict["_tel"], input_dict["__email_notification"], input_dict["__sms_notification"], input_dict["_address"]))
# def __init__(self, email, password, full_name, gender, tel, permission):
Sys.User_DB.append(Admin("test1", "$2b$12$.t3ijxAUbFl1QdYJ4qDAT.AeZ4AmLn78qnM963AI/nl3qsbLn5fxu", "L L", "What", "151515151", []))
print(Sys.get_password_hash("test1"))

pookantong_book1 = Book(
                       'random.png',
                       'ในคืนที่โหดร้ายพระเอกตายแต่.....',
                       'Pookantong',
                       'Pookantong1',
                       '250 หน้า ปกแข็ง',
                       'BanDao',
                       'yamete!',
                       'critic review',
                       [],
                       'พระเอกตาย',
                       ['comedy','adult','intense','violent','drama','romantic','Yuri','Yaoi','School life'],
                       '18/12/29999',
                       9,
                       999,
                       9)

pookan_admin555 = Admin("Pookan@gmail.com", "La", "Pookan", "Male", "488188561", [])

rangsit = Branch('rangsit',
                       '9:00-23:00',
                       'future park rangsit',
                       '0983868365',
                       'bookshop.rangsit',
                       'rangsit_bookshop')

batalog.add_book(pookantong_book1)
event = EventDiscount("dan",datetime.date(2023, 3, 31), datetime.date(2023, 4, 30), 0.9)
event.add_book_to_event(pookantong_book1)
bangkok = Branch("Bangkok",
                 "6.00 - 22.00",
                 "Bangkok",
                 "0864615559",
                 "bookshop.bangkok",
                 "bangkok_bookshop")

moon_branch = Branch('Moon',
                     '23:00 - 23:59',
                     'Moon',
                     '0995471568',
                     'bookshop.moon',
                     'moon_bookshop')

# all_branch.add_branch(rangsit)
# pookantong_rating1 = Rating(pookantong_book1, 10, "Bad ending, I don't like it")

def event_dis():
    for i in batalog.list_all_of_book:
        if i._name in [x._name for x in event.list_of_book]:
            event.apply_discount(i)

def find_book_in_catalog(name:Optional[str] = ''):
    searched = []
    if name != '':
        for i in batalog.list_all_of_book:
            if name.lower() in i._name.lower():
                searched.append(i)
    return searched

def get_book(name:Optional[str] = ''):
    if name != '':
        for i in batalog.list_all_of_book:
            if name.lower() == i._name.lower():
                return i
#################################  MAINPAGE  ####################################        
@app.get("/")
async def home(request:Request):
    event_dis()
    return templates.TemplateResponse("index.html", {"request":request,"book_list":batalog.get_all_list()})

@app.get("/search/")
async def show_book(request:Request,q: str):
    event_dis()
    return templates.TemplateResponse("index.html", {"request":request,"book_list":find_book_in_catalog(q)})

@app.get("/books/{book_name}")
async def view_book(request:Request,book_name:str):
    event_dis()
    return templates.TemplateResponse("bookdetail.html", {"request":request,"book":get_book(book_name)})

#################################  BASKETPAGE  ####################################  
@app.get("/basket")
async def basket(request:Request):
    return templates.TemplateResponse("cart.html", {"request":request,"basket_list":pookaneiei.basket})

#################################  BRANCH PAGE  #################################### 
@app.get("/branch/search/")
async def search_branch(request:Request, book_name:str):
    return templates.TemplateResponse("branch.html", {"request": request, "branch_list": shop.search_available_branch(book_name)})

@app.post("/add_basket")
async def add_book_to_basket(book:str = Form(...)):
    event_dis()
    book_item = get_book(book)
    pookaneiei.add_book_to_basket(BookItem(book_item),book_item)
    return RedirectResponse(url="/books/"+book, status_code=status.HTTP_302_FOUND)
@app.post("/add_amount")
async def add_book_to_basket(book:str = Form(...)):
    event_dis()
    pookaneiei.basket.add_amount(book)
    return RedirectResponse(url="/basket", status_code=status.HTTP_302_FOUND)
@app.post("/reduce_amount")
async def add_book_to_basket(book:str = Form(...)):
    event_dis()
    pookaneiei.basket.reduce_amount(book)
    return RedirectResponse(url="/basket", status_code=status.HTTP_302_FOUND)

#################################  ORDERPAGE  ####################################
@app.get("/order")
async def make_order(request:Request):
    order = Order(pookaneiei.basket.book_item,
                        random.randint(1000,9999),
                        False,
                        pookaneiei.basket.price,
                        pookaneiei)
    return templates.TemplateResponse("order.html", {"request":request,"order_list":order})

@app.post("/addbook")
async def add_book(data:AddBookDTO):
    batalog.add_book(Book(
                        data.cover,
                        data.brief,
                        data.creator,
                        data.name,
                        data.book_info,
                        data.book_publisher,
                        data.book_preview,
                        data.critic_review,
                        data.table_of_content,
                        data.summary,
                        data.genre,
                        data.date_created,
                        data.rating,
                        data.price,
                        data.amount)
                )
    return batalog.list_all_of_book

@app.post("/addbranch")
async def add_branch(data:AddBranchDTO):
    shop.add_branch(Branch(data.branch_name,
                data.open_time,
                data.location,
                data.tel,
                data.line_id,
                data.facebook_id))
    return shop.list_of_branch

@app.get("/basket")
async def basket():
    return pookaneiei.basket.book_item

@app.post("/basket")
async def make_order(data:MakeOrderDto):
    pookaneiei.make_order(Order(pookaneiei.basket.book_item,
                        pookaneiei.order_id,
                        data.status,
                        pookaneiei.basket.price,
                        pookaneiei))
    return pookaneiei.order_list

@app.get("/")
async def home():
    return {"Welcome to BookShop"}


@app.get("/GetCreditCard/")
async def get_credit_card(current_user = Depends(Sys.get_current_user)):
    return current_user.credit_card

@app.post("/AddCreditCard/")
async def add_credit_card(credit_card : CreditCardDTO, current_user = Depends(Sys.get_current_user)):
    current_user.add_credit_card(CreditCard(credit_card.card_num, credit_card.expire_date, credit_card.cvc))
    return {"Add CreditCard Success"}

# edit this
@app.put("/ModifyCreditCard/")
async def modify_credit_card(credit_card : CreditCardDTO, current_user = Depends(Sys.get_current_user)):
    current_user.credit_card.modify_credit_card_info(credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return {"Modify Success"}

@app.get("/GetAllBranch/")
async def get_branch():
    return shop.list_of_branch

@app.post("/AddBookToBranch/{branch_name}")
async def add_book_to_stock(branch_name, data:AddBookDTO):
    select_branch = shop.select_branch(branch_name)
    select_branch.add_book_to_stock(Book(
                        data.cover,
                        data.brief,
                        data.creator,
                        data.name,
                        data.book_info,
                        data.book_publisher,
                        data.book_preview,
                        data.critic_review,
                        data.table_of_content,
                        data.summary,
                        data.genre,
                        data.date_created,
                        data.rating,
                        data.price,
                        data.amount))
    return {"Add to stock Success"}

@app.post("/AddBranch")
async def add_branch(data:AddBranchDTO):
    shop.add_branch(Branch(data.branch_name,
                data.open_time,
                data.location,
                data.tel,
                data.line_id,
                data.facebook_id))
    return {"Add Branch Success"}

@app.put("/ModifyBranch/{branch_name}")
async def modify_branch(data : ModifyBranchDTO, branch_name):
    select_branch = shop.select_branch(branch_name)
    select_branch.modify_branch(data.branch_name, 
                                data.open_time, 
                                data.location, 
                                data.tel, 
                                data.line_id, 
                                data.facebook_id, 
                                data.add_book, 
                                data.remove_book)
    return {"Modify Success"}

@app.delete("/RemoveBranch/{branch_name}")
async def remove_branch(branch_name):
    select_branch = shop.select_branch(branch_name)
    shop.delete_branch(select_branch)
    return {"Remove Branch Success"}

@app.get("/GetAllEvent/")
async def get_event():
    return shop.list_of_event

@app.post("/AddEvent/")
async def add_event(data : EventDTO):
    shop.list_of_event(EventDiscount(data.event_name, 
                                    data.event_start, 
                                    data.event_end, 
                                    data.discounted_percentage))
    return {"Add Event Success"}

# we dont place to collect class bookshop
@app.put("/ModifyEvent/{event_name}")
async def modify_event(data : ModifyEventDTO, event_name):
    # loop check in bigger class
    select_event = shop.select_event(event_name)
    select_event.modify_event(data.event_name,
                              data.event_start,
                              data.event_end,
                              data.discounted_percentage)
    return {"Modify Success"}

@app.delete("/RemoveEvent/{event_name}")
async def delete_event(event_name):
    select_event = shop.select_event(event_name)
    shop.list_of_event.delete_event(select_event)
    return {"Remove This Event Success"}

@app.get("/Payment/Check")
async def check_payment(status : str):
    if status.lower() == "success":
        return {"success"}
    else:
        return {"reject"}

@app.get("/QrPayment/Generate/")
async def generate_qr(current_user = Depends(Sys.get_current_user)):
    transactions = ViaQrCode(current_user.basket.price, "04-07-2023")
    transactions.generate_qr_code()
    del transactions
    return FileResponse("../qrcode-0890767442.png")
    # redirect to check payment

@app.put("/book/{old_name}")
async def modify_book(old_name,book:ModifyBookDTO):
    for i in batalog.list_all_of_book:
        if old_name == i._name:
            select_book = i
    select_book.modify_book(book.cover,book.brief,book.creator,book.name,book.book_info,book.book_publisher,book.book_preview,book.critic_review,
                          book.table_of_content,book.summary,book.genre,book.date_created,book.price,book.amount_in_stock,)
    return select_book

async def get_current_active_user(current_user = Depends(Sys.get_current_user)) :
	# print(current_user.__dict__)
	if current_user._disabled :
		raise HTTPException(status_code=400, detail="Inactive User")
	return current_user

@app.put("/users/edit")
async def info_verification(email : Optional[str] = None, password : Optional[str] = None, full_name : Optional[str] = None, gender : Optional[str] = None, tel : Optional[str] = None, address : Optional[str] = None,
				email_noti : Optional[bool] = None, sms_noti : Optional[bool] = None, id = Depends(Sys.get_current_user)) :
	if (id == None) :
		return {"Error-101" : "Didn't find any account with this id"}
	elif (isinstance(id, Customer)) :
		id._email = email or id._email
		id._password = password or id._password
		id._full_name = full_name or id._full_name
		id._gender = gender or id._gender
		id._tel = tel or id._tel
		id._address = address or id._address
		# id._email_notification = email_noti if email_noti != None else id._email_notification
		# id._sms_notification = sms_noti if sms_noti != None else id._sms_notification
		if email_noti != None :
			id.email_notification = email_noti
		if email_noti != None :
			id.sms_notification = sms_noti
	elif (isinstance(id, Admin)) :
		id._email = email or id._email
		id._password = password or id._password
		id._full_name = full_name or id._full_name
		id._gender = gender or id._gender
		id._tel = tel or id._tel

@app.post("/token", response_model=Token)
async def login(form_data : OAuth2PasswordRequestForm = Depends()) :
	user = Sys.authenticate_user(form_data.username, form_data.password)
	if not user :
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password", headers={"WWW-Authenticate" : "Bearer"})
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
	access_token = Sys.creat_access_token(data={"sub" : user._email}, expires_delta=access_token_expires)
	return {"access_token" : access_token, "token_type" : "bearer"}

@app.get("/users/me")
async def view_info(userid = Depends(get_current_active_user)):
		return (userid)


@app.post("/users/registration")
async def registration(email : str , password : str, full_name : str, gender : str, tel : str, address : str,
				email_noti : bool, sms_noti : bool) :
	input_dict = {}
	input_dict['_email'] = email
	input_dict['_password'] = Sys.get_password_hash(password)
	input_dict['_full_name'] = full_name
	input_dict['_gender'] = gender
	input_dict['_tel'] = tel
	input_dict['_address'] = address
	input_dict['__email_notification'] = email_noti
	input_dict['__sms_notification'] = sms_noti

	# Sys.User_DB.append(pookaneiei)
	Sys.User_DB.append(Customer(input_dict["_email"], input_dict["_password"], input_dict["_full_name"], input_dict["_gender"], input_dict["_tel"], input_dict["__email_notification"], input_dict["__sms_notification"], input_dict["_address"]))

