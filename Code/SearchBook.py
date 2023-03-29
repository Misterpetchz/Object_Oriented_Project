from Modules.UserAccount import Customer
from Modules.Catalog import Catalog
from Modules.Book import BookItem

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
book1 = BookItem(4090,
                 'Element_Online_Phase4_1.png',
                 'online game',
                 'MASALAN',
                 'Element Online Phase 4.1',
                 'Hard cover with 388 page and 8 game card',
                 '978-616-00-2417-9',
                 'satapornbooks',
                 '1.....',
                 'Good Novel',
                 [],
                 'เกม EO อัปเดตแพตช์ที่มาพร้อมเมืองใหม่ นั้นคือ เกาะลอยฟ้า',
                 ['fantasy'],
                 '18-Mar-2016',
                 9,
                 10,
                 9)
batalog = Catalog([pookantong_book1, pookantong_book2, book1])
batalog.search_book(input())
print(batalog.list_of_book)