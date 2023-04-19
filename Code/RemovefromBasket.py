from Modules.UserAccount import Customer
from Modules.Book import *
from Modules.Catalog import Catalog
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
                       9
                       )

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
                 True
)
pookaneiei.add_book_to_basket(BookItem(
            pookantong_book1._cover,
            pookantong_book1._brief,
            pookantong_book1._creator,
            pookantong_book1._name,
            pookantong_book1._book_info,
            pookantong_book1._book_publisher,
            pookantong_book1._book_preview,
            pookantong_book1._critic_review,
            pookantong_book1._table_of_content,
            pookantong_book1._summary,
            pookantong_book1._genre,
            pookantong_book1._date_created,
            pookantong_book1._rating,
            pookantong_book1._price,
            0
            ),
            pookantong_book1)
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
            pookantong_book2._price,
            0
            ),
            pookantong_book2)
print(pookantong_book2._amount_in_stock)
pookaneiei.remove_book_from_basket(1,pookantong_book2)
print(pookantong_book2._amount_in_stock)