from UserAccount import *
from Book import *
from Rating import *
from EventDiscount import *
from Branch import *
from Coupon import *
from Basket import *
from Catalog import *
pookantong_book1 = BookItem(2547,
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
                       9,
                       999,
                       9)

pookantong_book2 = BookItem(9875,
                       'random2.png',
                       'ในคืนที่โหดร้ายนางเอกตายแต่.....',
                       'Pookantong',
                       'Pookantong2',
                       '999 หน้า ปกแข็ง',
                       '8572az0Kjd9',
                       'BanDao',
                       'yamete kudasai!',
                       'critic review',
                       [],
                       'นางเอกตาย',
                       ['Comedy','Adult','Intense','Violent','Drama','Romantic','Yuri','Yaoi','School life','Shounen']
                       ,'18/12/29999',
                       9,
                       999,
                       9)

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
batalog = Catalog([pookantong_book1, pookantong_book2])
pookaneiei.add_book_to_basket(batalog, pookantong_book1)
pookaneiei.add_book_to_basket(batalog, pookantong_book2)
print(pookaneiei._basket._book_item)
print(pookaneiei._basket._book_item[0]._name)
