from Modules.UserAccount import*
from Modules.Branch import Branch
from Modules.Book import BookItem
from Modules.BranchList import BranchList

pookaneiei = Customer('pookantong.p@gmail.com',
                 'PomyukmeFan555',
                 'PookanNaja',
                 'Male',
                 '0980231173',
                 [],
                 '29/7 หมู่2 ตำบลบั้นเด้า อำเภอรถแห่ จังหวัดสก๊อย ประเทศหิวข้าว ดาวSun',
                 True,
                 True)
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
bangkok = Branch("Bangkok",
                 "6.00 - 22.00",
                 "Bangkok",
                 "0864615559",
                 "bookshop.bangkok",
                 "bangkok_bookshop",
                 [pookantong_book1,pookantong_book2,book1])
nonthaburi1 = Branch("Nonthaburi",
                     "8:30-22:00",
                     "Nonthaburi",
                     "0811111111",
                     "seed_nonthaburi01",
                     "NonthaburiSE-ED",
                     [pookantong_book1,pookantong_book2])
rangsit = Branch('rangsit',
                       '9:00-23:00',
                       'future park rangsit',
                       '0983868365',
                       'bookshop.rangsit',
                       'rangsit_bookshop',
                       [pookantong_book2,book1])
moon_branch = Branch('Moon',
                     '23:00 - 23:59',
                     'Moon',
                     '0995471568',
                     'bookshop.moon',
                     'moon_bookshop'
                     ,[pookantong_book1])

all_branch = BranchList([bangkok,nonthaburi1,moon_branch,rangsit])
all_branch.search_available_branch(book1)
print(all_branch.available_branch)