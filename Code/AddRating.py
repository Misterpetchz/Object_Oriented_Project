from Modules.UserAccount import Customer
from Modules.Rating import Rating
from Modules.Book import BookItem

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
                       [],
                       999,
                       [])

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


pookantong_rating1 = Rating(pookantong_book1, 10, "Bad ending, I don't like it")
pookantong_rating2 = Rating(pookantong_book1, 9, "So Cool!")

pookaneiei.add_rating(pookantong_book1,pookantong_rating1)
pookaneiei.add_rating(pookantong_book1,pookantong_rating2)
print(pookantong_book1._rating[1]._book_rating)