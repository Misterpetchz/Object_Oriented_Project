from fastapi import FastAPI
from Modules.Catalog import Catalog
from Modules.EventDiscount import EventDiscount
from Modules.Book import Book,BookItem
from Modules.UserAccount import Customer
from CLassDTO import AddBookDTO
import datetime
app = FastAPI()

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
batalog.add_book(pookantong_book1)
event = EventDiscount("dan",datetime.date(2023, 3, 31), datetime.date(2023, 4, 30), 0.9)
event.add_book_to_event(pookantong_book1)

def event_dis():
    if datetime.datetime.now() > event.event_start and datetime.datetime.now() < event.event_end:
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
async def show_book(name:str):
    event_dis()
    return find_book_in_catalog(name)

@app.post("/books/{name}")
async def add_book_to_basket(book:AddBookDTO):
    event_dis()
    book_item = find_book_in_catalog(book.name)
    pookaneiei.add_book_to_basket(BookItem(
            book_item._cover,
            book_item._brief,
            book_item._creator,
            book_item._name,
            book_item._book_info,
            book_item._book_publisher,
            book_item._book_preview,
            book_item._critic_review,
            book_item._table_of_content,
            book_item._summary,
            book_item._genre,
            book_item._date_created,
            book_item._rating,
            book_item._new_price,
            ),find_book_in_catalog(book.name))
    return pookaneiei.basket.book_item