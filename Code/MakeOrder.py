from Modules.UserAccount import Customer
from Modules.Book import *
from Modules.Catalog import Catalog
from Modules.EventDiscount import EventDiscount
from Modules.Order import Order
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
pookaneiei = Customer('pookantong.p@gmail.com',
                 'PomyukmeFan555',
                 'PookanNaja',
                 'Male',
                 '0980231173',
                 [],
                 '29/7 หมู่2 ตำบลบั้นเด้า อำเภอรถแห่ จังหวัดสก๊อย ประเทศหิวข้าว ดาวSun',
                 True,
                 True,   
)
batalog = Catalog()
batalog.add_book(pookantong_book2)
pookaneiei.add_book_to_basket(BookItem(
            pookantong_book2._cover,
            pookantong_book2._brief,
            pookantong_book2._creator,
            pookantong_book2._name,
            pookantong_book2._book_info,
            pookantong_book2._book_publisher,
            pookantong_book2._book_preview,
            pookantong_book2._critic_review,
            pookantong_book2._table_of_content,
            pookantong_book2._summary,
            pookantong_book2._genre,
            pookantong_book2._date_created,
            pookantong_book2._rating,
            pookantong_book2._price
            ),
            pookantong_book2)
event = EventDiscount("dan",1,1,0.9)
event.add_book_to_event(pookantong_book2)
pookaneiei.make_order(Order(pookaneiei.basket,
                        pookaneiei.order_id,
                        False,
                        pookaneiei.basket.price,
                        pookaneiei))

print(pookaneiei.order_list)