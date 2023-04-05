from fastapi import FastAPI
from Modules.Catalog import Catalog
from Modules.EventDiscount import EventDiscount
from Modules.Book import Book,BookItem
from Modules.UserAccount import Customer
from Modules.Branch import Branch
from Modules.BranchList import BranchList
from Modules.Order import Order
from Modules.Rating import Rating
from CLassDTO import *
import datetime
import sys
sys.setrecursionlimit(1500)
app = FastAPI()



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




pookaneiei = Customer('pookantong.p@gmail.com',
                 'PomyukmeFan555',
                 'PookanNaja',
                 'Male',
                 '0980231173',
                 [],
                 '29/7 หมู่2 ตำบลบั้นเด้า อำเภอรถแห่ จังหวัดสก๊อย ประเทศหิวข้าว ดาวSun',
                 True,
                 True)





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
                       9,
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
                       9,
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




def event_dis():
    for i in batalog.list_all_of_book:
        if i._name in [x._name for x in event.list_of_book]:
            event.apply_discount(i)

def find_book_in_catalog(name):
    for i in batalog.list_all_of_book:
        if name == i._name:
            return i




@app.get("/")
async def home():
    event_dis()
    return batalog

@app.get("/books/{name}")
async def show_book(name:str,branch_available:bool | None = None):
    event_dis()
    if branch_available == True:
        all_branch.search_available_branch(find_book_in_catalog(name))
        return all_branch.available_branch
    return find_book_in_catalog(name)

@app.post("/books/{name}")
async def add_book_to_basket(book:AddBooktoBasketDTO):
    event_dis()
    book_item = find_book_in_catalog(book.name)
    pookaneiei.add_book_to_basket(BookItem(book_item),book_item)
    return pookaneiei.basket.book_item

@app.get("/books/{name}/rating")
async def show_book_rating(name):
    book = find_book_in_catalog(name)
    return book._rating

@app.post("/books/{name}/rating")
async def show_book_rating(name, data:AddRatingDTO):
    book:Book = find_book_in_catalog(name)
    book.add_rating(Rating(data.score, data.comment))
    return book


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
    all_branch.add_branch(Branch(data.branch_name,
                data.open_time,
                data.location,
                data.tel,
                data.line_id,
                data.facebook_id))
    return all_branch.list_of_branch

@app.get("/basket")
async def basket():
    return pookaneiei.basket.book_item

@app.post("/basket")
async def make_order(data:MakeOrderDto):
    pookaneiei.make_order(Order(pookaneiei.basket.book_item,
                                pookaneiei.order_id,
                                False
                                ,pookaneiei.basket.price
                                ,pookaneiei._full_name))
    return pookaneiei.order_list

@app.put("/basket")
async def remove_from_basket(data:RemoveBookDTO):
    book = find_book_in_catalog(data.book_name)
    pookaneiei.remove_book_from_basket(data.index,book)
    return pookaneiei.basket.book_item

@app.post("/search")
async def search_book(data:SearchBookDTO):
    event_dis()
    batalog.search_book(data.string)
    return batalog.list_of_book




    