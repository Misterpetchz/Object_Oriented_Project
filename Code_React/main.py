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
from fastapi.middleware.cors import CORSMiddleware
import io
import uuid
import re


app = FastAPI()

origins = {
	"http://localhost",
	"http://localhost:5173",
}

app.add_middleware(
CORSMiddleware,
	allow_origins = origins,
	allow_credentials =True,
	allow_methods = ["*"],
	allow_headers= ["*"],
)



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
shop.add_branch(bangkok)
shop.add_branch(nonthaburi1)
shop.add_branch(rangsit)
shop.add_branch(moon_branch)
pookaneiei1 = Customer("pookan@gmail.com", Sys.get_password_hash("test1"),
					"pookan", "Male", "0000000000", True, False, "LLL")
pookaneiei2 = Customer("pookan2@gmail.com", Sys.get_password_hash("test1"),
					"pookan", "Male", "0000000000", True, False, "LLL")
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

pookan_admin555 = Admin("Pookan@gmail.com", Sys.get_password_hash("123"),
						"Pookan", "Male", "488188561", [])

Sys.register(pookan_admin555)

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
					['Intense'],
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
					['School','Shounen'], '18/12/29999',
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

pookantong_book1.add_rating(Rating(10, "Bad ending, I don't like it", pookaneiei))
pookantong_book1.add_rating(Rating(5, "OK, I don't like it", pookaneiei2))
pookaneiei1.add_book_to_basket(BookItem(pookantong_book1),pookantong_book1)
pookaneiei1.add_book_to_basket(BookItem(pookantong_book2),pookantong_book2)
pookaneiei1.add_book_to_basket(BookItem(pookantong_book1),pookantong_book1)

event = EventDiscount("dan", datetime.date(2023, 3, 31),
					datetime.date(2023, 4, 30), 0.9, 'Shounen')


@app.get("/", tags=["books"])
async def home():
	event.event_dis(batalog)
	return {"catalog":[{"cover":x._cover,
						"name":x._name,
						"creator":x._creator,
						"old_price":x._price,
						"new_price":x._new_price,
						"genre":x._genre,
						"score":f'{x._rating_score:.2f}',
						"brief":x._brief}
					for x in batalog.list_all_of_book if x._amount_in_stock != 0]}

@app.get("/books/{bookname}", tags=["books"])
async def show_book(bookname:str | None = None):
	event.event_dis(batalog)
	book = batalog.find_book_by_name(bookname)
	if book == None:
		raise HTTPException(status_code=404, detail="Book not found")
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
			"score":f'{book._rating_score:.2f}',
			"brief":book._brief,
			"available_branch":[x._branch_name for x in shop.search_available_branch(book)]}


@app.get("/books/{bookname}/rating", tags=["books"])
async def show_book_rating(bookname):
	book = batalog.find_book_by_name(bookname)
	return {"rating_score": f'{book._rating_score:.2f}',
			"rating": [{"score_each_rating": x._book_rating,
					"comment": x._book_comment} for x in book._rating]}

@app.get("/basket", tags=["user"])
async def show_basket(current_user : Customer = Depends(Sys.get_current_user)):
	return {"basket":[{"cover":x._cover,
						"name":x._name,
						"price":x._price,
						"genre":x._genre,
						"amount":x._amount
						}
					for x in current_user.basket.book_item]}

@app.put("/basket/add_amount/{bookname}", tags=["user"])
async def add_amount(bookname:str, current_user : Customer = Depends(Sys.get_current_user)):
	book = batalog.find_book_by_name(bookname)
	current_user.add_amount(bookname,book)

@app.put("/basket/reduce_amount/{bookname}", tags=["user"])
async def reduce_amount(bookname:str, current_user : Customer = Depends(Sys.get_current_user)):
	book = batalog.find_book_by_name(bookname)
	current_user.reduce_amount(bookname,book)

@app.delete("/basket/delete_item/{bookname}", tags=["user"])
async def delete_amount(bookname:str, current_user : Customer = Depends(Sys.get_current_user)):
	book = batalog.find_book_by_name(bookname)
	current_user.delete_item(bookname,book)

@app.post("/books/{bookname}/add_book_to_basket", tags=["user"])
async def add_book_to_basket(bookname:str, amount:int, current_user : Customer = Depends(Sys.get_current_user)):
	event.event_dis(batalog)
	book = batalog.find_book_by_name(bookname)
	if book == None:
		raise HTTPException(status_code=404, detail="Book not found")
	for i in range(amount):
		current_user.add_book_to_basket(BookItem(book),book)
	return {"status":"Success"}


@app.post("/add_amount", tags=["user"])
async def add_book_to_basket(book_item, current_user : Customer = Depends(Sys.get_current_user)):
	event.event_dis(batalog)
	book = batalog.find_book_by_name(book_item)
	current_user.add_amount(book_item, book)
	return {"status":"Success"}


@app.post("/reduce_amount", tags=["user"])
async def add_book_to_basket(book_item, current_user : Customer = Depends(Sys.get_current_user)):
	event.event_dis(batalog)
	book = batalog.find_book_by_name(book_item)
	current_user.reduce_amount(book_item, book)
	return {"status":"Success"}

@app.get("/make_order", tags=["user"])
async def make_order(current_user : Customer = Depends(Sys.get_current_user)):
	current_user.make_order(Order(current_user.basket.book_item,
								current_user.order_id,
								True,
								current_user.basket.price,
								current_user._full_name))
	current_user.basket.book_item = []
	return {"payment_id" : current_user.payment_id}


@app.post("/books/{bookname}/addrating", tags=["books"])
async def add_rating(bookname, data: AddRatingDTO, current_user : Customer = Depends(Sys.get_current_user)):
	book: Book = batalog.find_book_by_name(bookname)
	if current_user not in [x._user for x in book._rating]:
		book.add_rating(Rating(data.score, data.comment, current_user))
	return {"status": "Success"}


@app.post("/addbook", tags=["books"])
async def add_book_to_catalog(data: AddBookDTO):
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
	return {"status": "Success"}

'''
@app.post("/addbranch", tags=["branch"])
async def add_branch_to_branch_list(data: AddBranchDTO):
	shop.add_branch(Branch(data.branch_name,
				data.open_time,
				data.location,
				data.tel,
				data.line_id,
				data.facebook_id))
	return {"status": "Success"}
'''
@app.get("/CreditCard/", tags=["user"])
async def print_credit_card(current_user = Depends(Sys.get_current_user)):
	if (isinstance(current_user, Customer) and current_user.credit_card != None) :
		card = current_user.credit_card
		return {"credit_card_num" : card.card_num,
				"credit_card_exp" : card.expire_date,
				"credit_card_cvc" : card.cvc}
	else :
		return {"status" : "Error"}

@app.post("/CreditCard/add", tags=["user"])
async def add_credit_card(credit_card: CreditCards, current_user = Depends(Sys.get_current_user)):
	current_user.add_credit_card(CreditCard(credit_card.card_num,
											credit_card.expire_date,
											credit_card.cvc))
	return {"status": "Success"}

# loop to get credit card object


@app.put("/Creditcard/edit", tags=["user"])
async def modify_credit_card(credit_card: CreditCards, current_user = Depends(Sys.get_current_user)):
	if (bool(re.match(r"[0-9]{2}/[0-9]{2}", credit_card.expire_date))
	and bool(re.match(r"[0-9]{16}", credit_card.card_num))
	and bool(re.match(r"[0-9]{3}", credit_card.cvc))) :
		if (current_user.credit_card == None) :
			current_user.add_credit_card(CreditCard(credit_card.card_num,
													credit_card.expire_date,
													credit_card.cvc))
		else :
			current_user.credit_card.modify_credit_card_info(
				credit_card.card_num, credit_card.expire_date, credit_card.cvc)
		return {"status": "Success"}
	else :
		return {"status": "Error"}


@app.post("/branch/search/", tags=["branch"])
async def search_branch(name:str):
	return {"branch":[{"name":x.branch_name,
						"open":x.open_time,
						"location":x.location,
						"tel":x.tel,
						"line_id":x.line_id,
						"facebook_id":x.facebook_id,
						"product":x.product_in_stock
						}
					for x in shop.search_branch(name)]}
 
@app.get("/branch/{name}", tags=["branch"])
async def view_branch(name:str):
    x = shop.select_branch(name)
    if x == None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return {"name":x.branch_name,
			"open":x.open_time,
			"location":x.location,
			"tel":x.tel,
			"line_id":x.line_id,
			"facebook_id":x.facebook_id,
			"product":x.product_in_stock
			}


@app.put("/books/{bookname}", tags=["books"])
async def modify_book_to_catalog(bookname, data:ModifyBookDTO):
	book = batalog.find_book_by_name(bookname)
	book.modify_book(data)
	return {"status":"Success"}



@app.put("/users/edit", tags=["user"])
async def info_verification(data: EditProfile,id=Depends(Sys.get_current_user)):
	if (id == None):
		return {"Error-101": "Didn't find any account with this id"}
	elif (isinstance(id, Customer)):
		id._password = data.password or id._password
		id._full_name = data.full_name or id._full_name
		id._gender = data.gender or id._gender
		id._tel = data.tel or id._tel
		id._address = data.address or id._address
		# id._email_notification = email_noti if email_noti != None else id._email_notification
		# id._sms_notification = sms_noti if sms_noti != None else id._sms_notification
		if data.email_noti != None:
			id.email_notification = data.email_noti
		if data.email_noti != None:
			id.sms_notification = data.sms_noti
		return {"status":"Success"}
	elif (isinstance(id, Admin)):
		id._password = data.password or id._password
		id._full_name = data.full_name or id._full_name
		id._gender = data.gender or id._gender
		id._tel = data.tel or id._tel
		return {"status":"Success"}



@app.post("/token", response_model=Token, tags=["user"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
	user = Sys.authenticate_user(form_data.username, form_data.password)
	if not user:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
							detail="Incorrect Username or Password", headers={"WWW-Authenticate": "Bearer"})
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
	access_token = Sys.creat_access_token(
		data={"sub": user._email}, expires_delta=access_token_expires)
	return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", tags=["user"])
async def view_info(userid=Depends(Sys.get_current_user)):
	return {"address" : userid._address,
			"email ": userid._email,
			"full_name" : userid._full_name,
			"gender": userid._gender,
			"tel": userid._tel,
	}

@app.get("/user", tags=["user"])
async def view_info(userid=Depends(Sys.get_current_user)):
	return {"address" : userid._address,
			"full_name" : userid._full_name,
			"gender": userid._gender,
			"tel": userid._tel,
			"email_noti": userid.email_notification,
			"sms_noti": userid.sms_notification
	}

@app.post("/users/registration", tags=["user"])
async def registration(data:RegisterDTO):
	if data.email in [x._email for x in Sys.User_DB]:
		return {"status":"Reject"}
	input_dict = {}
	input_dict['_email'] = data.email
	input_dict['_password'] = Sys.get_password_hash(data.password)
	input_dict['_full_name'] = data.full_name
	input_dict['_gender'] = data.gender
	input_dict['_tel'] = data.tel
	input_dict['_address'] = data.address
	input_dict['__email_notification'] = data.email_noti
	input_dict['__sms_notification'] = data.sms_noti
	Sys.register(Customer(input_dict["_email"], input_dict["_password"], input_dict["_full_name"], input_dict["_gender"], input_dict["_tel"], input_dict["__email_notification"], input_dict["__sms_notification"], input_dict["_address"]))

	return {"status":"Success"}

@app.put("/remove_basket", tags=["user"])
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
						"score":f'{x._rating_score:.2f}',
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

@app.get("/GetAllBranch/", tags=["branch"])
async def get_branch():
	return {"name" : [{"branch_name" :x._branch_name} for x in shop.list_of_branch] }

@app.post("/AddBookToBranch/{branch_name}", tags=["branch"])
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

@app.put("/ModifyBranch/{branch_name}", tags=["branch"])
async def modify_branch(data : ModifyBranchDTO, branch_name):
	select_branch = shop.select_branch(branch_name)
	select_branch.modify_branch(data.branch_name,
								data.open_time,
								data.location,
								data.tel,
								data.line_id,
								data.facebook_id,
								[],
								[])
	return {"Modify Success"}

@app.delete("/RemoveBranch/{branch_name}", tags=["branch"])
async def remove_branch(branch_name):
	select_branch = shop.select_branch(branch_name)
	shop.delete_branch(select_branch._branch_name)
	return {"Remove Branch Success"}

@app.get("/GetAllEvent/", tags=["event"])
async def get_event():
	return {"eventDis" : [{"event_name": x.event_name,
						"genre": x.event_genre} for x in shop.list_of_event]}

@app.post("/AddEvent/", tags=["event"])
async def add_event(data : EventDTO):
	shop.list_of_event.append((EventDiscount(data.event_name,
									data.event_start,
									data.event_end,
									data.discounted_percentage,
									data.event_genre)))
	return {"Add Event Success"}

# we dont place to collect class bookshop
@app.put("/ModifyEvent/{event_name}", tags=["event"])
async def modify_event(data : ModifyEventDTO, event_name):
	# loop check in bigger class
	select_event = shop.select_event(event_name)
	select_event.modify_event(data.event_name,
							data.event_start,
							data.event_end,
							data.discounted_percentage,
							data.event_genre)
	return {"Modify Success"}

@app.delete("/RemoveEvent/{event_name}", tags=["event"])
async def delete_event(event_name):
	select_event = shop.select_event(event_name)
	shop.delete_event(select_event.event_name)
	return {"Remove This Event Success"}

@app.get("/make_order", tags=["user"])
async def make_order(current_user : Customer = Depends(Sys.get_current_user)):
	current_user.make_order(Order(current_user.basket.book_item,
								current_user.order_id,
								True,
								current_user.basket.price,
								current_user._full_name))
	current_user.basket.book_item = []
	return {"payment_id" : current_user.payment_id}

@app.get('/payment/{id}')
async def get_payment(id, current_user = Depends(Sys.get_current_user), payment_type:str = None):
	if id == current_user.payment_id:
		if payment_type is None:
			return current_user.order
		elif payment_type.lower() == 'qrcode':
			return {"payment" : current_user.make_payment(payment_type) }
		elif payment_type.lower() == 'creditcard':
			# return info credit card
			current_user.make_payment(payment_type)
			return {"payment" : {'card_num' : current_user.credit_card.card_num,
								'expire_date' : current_user.credit_card.expire_date}}

# Check Status api
@app.get('/payment_status/{id}')
async def check_payment(id, current_user = Depends(Sys.get_current_user)):
	if id == current_user.payment_id:
		if current_user.payment.status == 'paid':
			current_user.add_order_to_order_list(current_user.order)
			current_user.update_order_id()
			current_user.reset_payment()
			return {"status" : 'paid'}
		# return {"status" : current_user.payment.status}

# Bank api
@app.post('/payment_status/{id}')
async def fake_bank(id, status:str = None):
	user = Sys.find_user_by_payment_id(id)
	user.payment.check_status(status)

# Order List after Payment Success
@app.get('/order_list/')
async def show_order_list(current_user = Depends(Sys.get_current_user)):
	return {'order_list' : current_user.order_list}


async def get_current_active_user(current_user = Depends(Sys.get_current_user)) :
	# print(current_user.__dict__)
	if current_user._disabled :
		raise HTTPException(status_code=400, detail="Inactive User")
	return current_user
