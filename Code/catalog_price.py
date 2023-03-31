from Modules.Book import*
from Modules.Catalog import*
from Modules.EventDiscount import*
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
                       9)
book1 = Book(
                 'Element_Online_Phase4_1.png',
                 'online game',
                 'MASALAN',
                 'Element Online Phase 4.1',
                 'Hard cover with 388 page and 8 game card',
                 
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
batalog = Catalog()
batalog.add_book(book1)
batalog.add_book(pookantong_book1)
batalog.add_book(pookantong_book2)
event = EventDiscount("dan",1,1,0.9)
event.add_book_to_event(pookantong_book2)
for i in batalog.list_all_of_book:
    if i._name in [x._name for x in event.list_of_book]:
        event.apply_discount(i)
print(batalog.list_all_of_book[2]._new_price)