from fastapi import BackgroundTasks, FastAPI, Request ,Form,Response
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import FileResponse, HTMLResponse
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
from Modules.Payment import *
from Modules.dto import *
from Modules.settings import *
from CLassDTO import *
from datetime import datetime
import random
import datetime
import starlette.status as status

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static",
    StaticFiles(directory="static"),
    name="static")

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

all_branch = BranchList()
bangkok = Branch("Bangkok",
                 "6.00 - 22.00",
                 "Bangkok",
                 "0864615559",
                 "bookshop.bangkok",
                 "bangkok_bookshop",
                 )
nonthaburi1 = Branch("Nonthaburi",
                     "8:30-22:00",
                     "Nonthaburi",
                     "0811111111",
                     "seed_nonthaburi01",
                     "NonthaburiSE-ED",
                     )
rangsit = Branch('rangsit',
                       '9:00-23:00',
                       'future park rangsit',
                       '0983868365',
                       'bookshop.rangsit',
                       'rangsit_bookshop',
                       )
moon_branch = Branch('Moon',
                     '23:00 - 23:59',
                     'Moon',
                     '0995471568',
                     'bookshop.moon',
                     'moon_bookshop'
                     )
all_branch.add_branch(bangkok)
all_branch.add_branch(nonthaburi1)
all_branch.add_branch(rangsit)
all_branch.add_branch(moon_branch)



pookaneiei1 = Customer("pookan@gmail.com", Sys.get_password_hash("test1"), "pookan", "Male", "0000000000", True, False, "LLL")
pookaneiei = Customer('pookantong.p@gmail.com',
                 Sys.get_password_hash("test2"),
                 'PookanNaja',
                 'Male',
                 '0980231173',
                 True,
                 True,
                 '29/7 หมู่2 ตำบลบั้นเด้า อำเภอรถแห่ จังหวัดสก๊อย ประเทศหิวข้าว ดาวSun')
Sys.register(pookaneiei)
Sys.register(pookaneiei1)





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
                       ['Comedy','Adult','Intense','Violent','Drama','Romantic','Yuri','Yaoi','School life'],
                       '18/12/29999',
                       999,
                       10)
pookantong_book2 = Book(
                       'random2.png',
                       'ในคืนที่โหดร้ายนางเอกตายแต่.....',
                       'Pookantong',
                       'Pookantong2',
                       '999 หน้า ปกแข็ง',
                       'BanDao',
                       'yamete kudasai!',
                       'critic review',
                       [],
                       'นางเอกตาย',
                       ['Comedy','Adult','Intense','Violent','Drama','Romantic','Yuri','Yaoi','School life','Shounen']
                       ,'18/12/29999',
                       999,
                       9
                       )
batalog.add_book(pookantong_book1)
batalog.add_book(pookantong_book2)
nonthaburi1.add_product(pookantong_book1)
nonthaburi1.add_product(pookantong_book2)
bangkok.add_product(pookantong_book1)
moon_branch.add_product(pookantong_book2)
rangsit.add_product(pookantong_book1)
rangsit.add_product(pookantong_book2)




event = EventDiscount("dan",datetime.date(2023, 3, 31), datetime.date(2023, 4, 30), 0.9, 'Shounen')




pookantong_book1.add_rating(Rating(10, "Bad ending, I don't like it"))
pookantong_book1.add_rating(Rating(5, "OK, I don't like it"))



pookaneiei.add_book_to_basket(BookItem(pookantong_book1),pookantong_book1)
pookaneiei.add_book_to_basket(BookItem(pookantong_book2),pookantong_book2)





async def get_current_active_user(current_user : Customer = Depends(Sys.get_current_user)) :
	# print(current_user.__dict__)
	if current_user._disabled :
		raise HTTPException(status_code=400, detail="Inactive User")
	return current_user



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
    event.event_dis(batalog)
    return templates.TemplateResponse("index.html", {"request":request,"book_list":batalog.get_all_list()})

@app.get("/search/")
async def show_book(request:Request,q: str):
    event.event_dis(batalog)
    return templates.TemplateResponse("index.html", {"request":request,"book_list":find_book_in_catalog(q)})

@app.get("/books", tags=["books"])
async def home():
    event.event_dis(batalog)
    return {"catalog":[{"cover":x._cover,
                        "name":x._name,
                        "creator":x._creator,
                        "old_price":x._price,
                        "new_price":x._new_price,
                        "genre":x._genre,
                        "score":x._rating_score,
                        "brief":x._brief}
                       for x in batalog.list_all_of_book if x._amount_in_stock != 0]}

@app.get("/books/{bookname}", tags=["books"])
async def show_book(bookname:str,branch_available:bool | None = None):
    event.event_dis(batalog)
    book = batalog.find_book_by_name(bookname)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found")
    if branch_available == True:
        all_branch.search_available_branch(batalog.find_book_by_name(bookname))
        return all_branch.available_branch
    return {"cover":book._cover,
            "name":book._name,
            "creator":book._creator,
            "info":book._book_info,
            "publisher":book._book_publisher,
            "preview":book._book_preview,
            "critic_review":book._critic_review,
            "table_of_content":book._table_of_content,
            "summary":book._summary,
            "date_created":book._date_created,
            "old_price":book._price,
            "new_price":book._new_price,
            "genre":book._genre,
            "score":book._rating_score,
            "brief":book._brief}

@app.post("/books/{bookname}/add_book_to_basket", tags=["user"])
async def add_book_to_basket(bookname:str, amount:int, current_user : Customer = Depends(Sys.get_current_user)):
    event.event_dis(batalog)
    book = batalog.find_book_by_name(bookname)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found")
    for i in range(amount):
        current_user.add_book_to_basket(BookItem(book),book)
    return {"status":"Success"}

@app.get("/books/{book_name}")
async def view_book(request:Request,book_name:str):
    event.event_dis(batalog)
    return templates.TemplateResponse("bookdetail.html", {"request":request,"book":get_book(book_name)})

#################################  BASKETPAGE  ####################################  
@app.get("/basket")
async def basket(request:Request):
    return templates.TemplateResponse("cart.html", {"request":request,"basket_list":pookaneiei.basket})
@app.get("/books/{bookname}/rating", tags=["books"])
async def show_book_rating(bookname):
    book = batalog.find_book_by_name(bookname)
    return {"rating_score":book._rating_score,
            "rating":[{"score_each_rating":x._book_rating,
                       "comment":x._book_comment} for x in book._rating]}

@app.post("/add_basket")
async def add_book_to_basket(book:str = Form(...)):
    event.event_dis(batalog)
    book_item = get_book(book)
    pookaneiei.add_book_to_basket(BookItem(book_item),book_item)
    return RedirectResponse(url="/books/"+book, status_code=status.HTTP_302_FOUND)
@app.post("/add_amount")
async def add_book_to_basket(book:str = Form(...)):
    event.event_dis(batalog)
    pookaneiei.basket.add_amount(book)
    return RedirectResponse(url="/basket", status_code=status.HTTP_302_FOUND)
@app.post("/reduce_amount")
async def add_book_to_basket(book:str = Form(...)):
    event.event_dis(batalog)
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
@app.post("/books/{bookname}/addrating", tags=["books"])
async def add_rating(bookname, data:AddRatingDTO):
    book:Book = batalog.find_book_by_name(bookname)
    book.add_rating(Rating(data.score, data.comment))
    return {"status":"Success"}

@app.post("/addbook", tags=["books"])
async def add_book_to_catalog(data:AddBookDTO):
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
            data.price,
            data.amount)
    )
    return {"status":"Success"}

@app.post("/addbranch", tags=["branch"])
async def add_branch_to_branch_list(data:AddBranchDTO):
    all_branch.add_branch(Branch(data.branch_name,
                data.open_time,
                data.location,
                data.tel,
                data.line_id,
                data.facebook_id))
    return {"status":"Success"}

@app.get("/")
async def home():
    return {"Welcome to BookShop"}

@app.post("/CreditCard/")
async def add_credit_card(credit_card : CreditCards):
    list_credit_card.append(CreditCard(credit_card.card_num, credit_card.expire_date, credit_card.cvc))
    return list_credit_card

# loop to get credit card object
@app.put("/creditcard/", tags=["user"])
async def modify_credit_card(credit_card : CreditCards):
    pookan_card.modify_credit_card_info(credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return pookan_card.__dict__

@app.put("/branch/", tags=["branch"])
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

async def get_current_active_user(current_user = Depends(Sys.get_current_user)) :
	# print(current_user.__dict__)
	if current_user._disabled :
		raise HTTPException(status_code=400, detail="Inactive User")
	return current_user

@app.put("/users/edit", tags=["user"])
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
	Sys.register(Customer(input_dict["_email"], input_dict["_password"], input_dict["_full_name"], input_dict["_gender"], input_dict["_tel"], input_dict["__email_notification"], input_dict["__sms_notification"], input_dict["_address"]))
	return {"status":"Success"}

@app.put("/basket", tags=["user"])
async def remove_from_basket(data:RemoveBookDTO, current_user : Customer = Depends(Sys.get_current_user)):
    book = batalog.find_book_by_name(data.book_name)
    current_user.remove_book_from_basket(data.index,book)
    return {"status":"Success"}

@app.post("/search", tags=["books"])
async def search_book(name:str):
    event.event_dis(batalog)
    batalog.search_book(name)
    return {"searchlist":[{"cover":x._cover,
                        "name":x._name,
                        "creator":x._creator,
                        "old_price":x._price,
                        "new_price":x._new_price,
                        "genre":x._genre,
                        "score":x._rating_score,
                        "brief":x._brief}
                       for x in batalog.list_of_book if x._amount_in_stock != 0]}
    
@app.put("/books/{bookname}", tags=["books"])
async def modify_book_to_catalog(bookname, data:ModifyBookDTO):
    book = batalog.find_book_by_name(bookname)
    book.modify_book(data)
    return {"status":"Success"}

@app.delete("/books/{bookname}", tags=["books"])
async def delete_book(bookname):
    book = batalog.find_book_by_name(bookname)
    batalog.remove_book(book)
    return {"status":"Success"}