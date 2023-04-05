from fastapi import FastAPI
from Modules.Catalog import Catalog
from Modules.EventDiscount import EventDiscount
from Modules.Book import *
from Modules.UserAccount import *
from Modules.settings import *
from Modules.BranchList import BranchList
from Modules.Branch import Branch
from Modules.Order import Order
from Modules.CreditCard import CreditCard
from Modules.Rating import Rating
from Modules.UserAccount import *
from Modules.dto import *
from CLassDTO import *
from datetime import datetime
import datetime

app = FastAPI()

list_credit_card = []
list_branch = BranchList()
User_DB = []


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



pookaneiei1 = Customer("pookan@gmail.com", "Test1", "pookan", "Male", "0000000000", True, False, "LLL")
pookaneiei = Customer('pookantong.p@gmail.com',
                 'PomyukmeFan555',
                 'PookanNaja',
                 'Male',
                 '0980231173',
                 True,
                 True,
                 '29/7 หมู่2 ตำบลบั้นเด้า อำเภอรถแห่ จังหวัดสก๊อย ประเทศหิวข้าว ดาวSun')





batalog = Catalog()

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
                       999,
                       9)
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




event = EventDiscount("dan",datetime.date(2023, 3, 31), datetime.date(2023, 4, 30), 0.9)
event.add_book_to_event(pookantong_book1)




pookantong_book1.add_rating(Rating(10, "Bad ending, I don't like it"))




pookaneiei.add_book_to_basket(BookItem(pookantong_book1),pookantong_book1)
pookaneiei.add_book_to_basket(BookItem(pookantong_book2),pookantong_book2)





async def get_current_active_user(current_user : Customer = Depends(Customer.get_current_user)) :
	# print(current_user.__dict__)
	if current_user._disabled :
		raise HTTPException(status_code=400, detail="Inactive User")
	return current_user





@app.get("/")
async def home():
    event.event_dis(batalog)
    return batalog

@app.get("/{bookname}")
async def show_book(bookname:str,branch_available:bool | None = None):
    event.event_dis(batalog)
    if branch_available == True:
        all_branch.search_available_branch(batalog.find_book_by_name(bookname))
        return all_branch.available_branch
    return batalog.find_book_by_name(bookname)

@app.post("/{book_name}/add_book_to_basket")
async def add_book_to_basket(book_name:AddBooktoBasketDTO, current_user : Customer = Depends(Customer.get_current_user)):
    event.event_dis(batalog)
    book_item = batalog.find_book_by_name(book_name)
    current_user.add_book_to_basket(BookItem(book_item),book_item)
    return current_user.basket.book_item

@app.get("{bookname}/rating")
async def show_book_rating(bookname):
    book = batalog.find_book_by_name(bookname)
    return book._rating

@app.post("{bookname}/addrating")
async def add_rating(bookname, data:AddRatingDTO):
    book:Book = batalog.find_book_by_name(bookname)
    book.add_rating(Rating(data.score, data.comment))
    return book

@app.post("/addbook")
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
    return batalog.list_all_of_book

@app.post("/addbranch")
async def add_branch_to_branch_list(data:AddBranchDTO):
    all_branch.add_branch(Branch(data.branch_name,
                data.open_time,
                data.location,
                data.tel,
                data.line_id,
                data.facebook_id))
    return all_branch.list_of_branch

@app.get("/basket")
async def show_basket():
    return pookaneiei.basket.book_item

@app.post("/make_order")
async def make_order(data:MakeOrderDto):
    pookaneiei.make_order(Order(pookaneiei.basket.book_item,
                                pookaneiei.order_id,
                                data.status
                                ,pookaneiei.basket.price
                                ,pookaneiei._full_name))
    return pookaneiei.order_list

@app.post("/creditcard/")
async def add_credit_card(credit_card : CreditCards):
    list_credit_card.append(CreditCard(credit_card.card_num, credit_card.expire_date, credit_card.cvc))
    return list_credit_card

# loop to get credit card object
@app.put("/creditcard/")
async def modify_credit_card(credit_card : CreditCards):
    pookan_card.modify_credit_card_info(credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return pookan_card.__dict__

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

@app.put("/users/edit")
async def info_verification(email : Optional[str] = None, password : Optional[str] = None, full_name : Optional[str] = None, gender : Optional[str] = None, tel : Optional[str] = None, address : Optional[str] = None,
				email_noti : Optional[bool] = None, sms_noti : Optional[bool] = None, id : Customer = Depends(Customer.get_current_user)) :
	if (id == None) :
		return {"Error-101" : "Didn't find any account with this id"}
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

@app.post("/token", response_model=Token)
async def login(form_data : OAuth2PasswordRequestForm = Depends()) :
	user = Customer.authenticate_user(form_data.username, form_data.password)
	if not user :
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password", headers={"WWW-Authenticate" : "Bearer"})
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
	access_token = Customer.creat_access_token(data={"sub" : user._email}, expires_delta=access_token_expires)
	return {"access_token" : access_token, "token_type" : "bearer"}

@app.get("/users/me")
async def view_info(userid : Customer = Depends(get_current_active_user)):
		return (userid)


@app.put("/users/registration")
async def registration(email : str , password : str, full_name : str, gender : str, tel : str, address : str,
				email_noti : bool, sms_noti : bool) :
	input_dict = {}
	input_dict['_email'] = email
	input_dict['_password'] = Customer.get_password_hash(password)
	input_dict['_full_name'] = full_name
	input_dict['_gender'] = gender
	input_dict['_tel'] = tel
	input_dict['_address'] = address
	input_dict['__email_notification'] = email_noti
	input_dict['__sms_notification'] = sms_noti

	User_DB.append(Customer(input_dict["_email"], input_dict["_password"], input_dict["_full_name"], input_dict["_gender"], input_dict["_tel"], input_dict["__email_notification"], input_dict["__sms_notification"], input_dict["_address"]))


@app.put("/basket")
async def remove_from_basket(data:RemoveBookDTO):
    book = batalog.find_book_by_name(data.book_name)
    pookaneiei.remove_book_from_basket(data.index,book)
    return pookaneiei.basket.book_item

@app.post("/search")
async def search_book(data:SearchBookDTO):
    event.event_dis(batalog)
    batalog.search_book(data.string)
    return batalog.list_of_book




    