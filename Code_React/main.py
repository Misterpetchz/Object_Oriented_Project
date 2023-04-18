from fastapi import FastAPI
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
from datetime import datetime
import random
import datetime
import starlette.status as status
from fastapi.middleware.cors import CORSMiddleware


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



Sys = System()


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
                       ['comedy', 'adult', 'intense', 'violent', 'drama',
                           'romantic', 'Yuri', 'Yaoi', 'School life'],
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
                       ['Comedy', 'Adult', 'Intense', 'Violent', 'Drama', 'Romantic',
                           'Yuri', 'Yaoi', 'School life', 'Shounen'], '18/12/29999',
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
                        "score":x._rating_score,
                        "brief":x._brief}
                       for x in batalog.list_all_of_book if x._amount_in_stock != 0]}

@app.get("/books/{bookname}", tags=["books"])
async def show_book(bookname:str | None = None):
    event.event_dis(batalog)
    book = batalog.find_book_by_name(bookname)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found")
    all_branch.search_available_branch(book)
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
            "available_branch":[x._branch_name for x in all_branch.available_branch]}


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
    return {"status":"Success"}


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


@app.post("/addbranch", tags=["branch"])
async def add_branch_to_branch_list(data: AddBranchDTO):
    all_branch.add_branch(Branch(data.branch_name,
                data.open_time,
                data.location,
                data.tel,
                data.line_id,
                data.facebook_id))
    return {"status": "Success"}


@app.post("/CreditCard/", tags=["user"])
async def add_credit_card(credit_card: CreditCards, current_user = Depends(Sys.get_current_user)):
    current_user.add_credit_card(CreditCard(credit_card.card_num,
                                            credit_card.expire_date,
                                            credit_card.cvc))
    return {"status": "Success"}

# loop to get credit card object


@app.put("/creditcard/", tags=["user"])
async def modify_credit_card(credit_card: CreditCards, current_user = Depends(Sys.get_current_user)):
    current_user.credit_card.modify_credit_card_info(
        credit_card.card_num, credit_card.expire_date, credit_card.cvc)
    return {"status": "Success"}


@app.post("/branch/", tags=["branch"])
async def add_branch(branch: Branchs):
    pookan_admin555.add_branch(all_branch, branch)
    return {"status":"Success"}


@app.put("/branch/", tags=["branch"])
# loop to get branch object
async def modify_branch(branch: dict):
    branch_name = branch["branch_name"]
    open_time = branch["open_time"]
    location = branch["location"]
    tel = branch["tel"]
    line_id = branch["line_id"]
    facebook_id = branch["facebook_id"]
    rangsit.modify_branch(branch_name, open_time, location,
                          tel, line_id, facebook_id, [], [])
    return {"status":"Success"}


@app.put("/books/{bookname}", tags=["books"])
async def modify_book_to_catalog(bookname, data:ModifyBookDTO):
    book = batalog.find_book_by_name(bookname)
    book.modify_book(data)
    return {"status":"Success"}



@app.put("/users/edit", tags=["user"])
async def info_verification(password: Optional[str] = None, full_name: Optional[str] = None, gender: Optional[str] = None, tel: Optional[str] = None, address: Optional[str] = None,
				email_noti: Optional[bool] = None, sms_noti: Optional[bool] = None, id=Depends(Sys.get_current_user)):
	if (id == None):
		return {"Error-101": "Didn't find any account with this id"}
	elif (isinstance(id, Customer)):
		id._password = password or id._password
		id._full_name = full_name or id._full_name
		id._gender = gender or id._gender
		id._tel = tel or id._tel
		id._address = address or id._address
		# id._email_notification = email_noti if email_noti != None else id._email_notification
		# id._sms_notification = sms_noti if sms_noti != None else id._sms_notification
		if email_noti != None:
			id.email_notification = email_noti
		if email_noti != None:
			id.sms_notification = sms_noti
		return {"status":"Success"}
	elif (isinstance(id, Admin)):
		id._password = password or id._password
		id._full_name = full_name or id._full_name
		id._gender = gender or id._gender
		id._tel = tel or id._tel
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


@app.post("/users/registration", tags=["user"])
async def registration(data:RegisterDTO):
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