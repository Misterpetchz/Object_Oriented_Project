from Modules.UserAccount import Admin
from Modules.EventDiscount import EventDiscount
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

pookan_admin555 = Admin('65010895@kmitl.ac.th',
                 'PomyukmeFan55',
                 'Yotsapat',
                 'Male',
                 '0980231172',
                 [],
                 True)

book_lover = EventDiscount("Book Lover",
                            "18-Mar-23",
                            "30-Mar-23",
                            [],
                            [],
                            pookantong_book1)

pookan_admin555.add_event(pookantong_book1, book_lover)
print(pookantong_book1.event_discount[0].event_name)