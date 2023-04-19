from UserAccount import *
from Book import BookItem
import Rating
import EventDiscount
import Branch
import Coupon
import Basket
#-------------------------------------------------------------------------------------------------------------------
#Book
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
                       Rating,
                       999,
                       EventDiscount)

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
                       Rating,
                       999,
                       EventDiscount)

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
                 Rating,
                 10,
                 EventDiscount)

book2 = BookItem(1080,
                 'แค่ใช้คำให้ฉลาด.png',
                 'tips',
                 'ซาซากิ เคอิจิ',
                 'แค่ใช้คำให้ฉลาดก็เพิ่มโอกาสจาก 0 เป็น 100',
                 'Hard cover with 214 page',
                 '978-616-287-089-7',
                 'วีเลิร์น',
                 '1......',
                 'Good book tips',
                 [],
                 'การใช้คำให้ฉลาดจะสามารถเพิ่มโอกาสได้',
                 ['self-help book'],
                 '1-Jan-2013',
                 Rating,
                 20,
                 EventDiscount)

book3 = BookItem(78254,
                 "cover78254.png",
                 "Leave now, Human. You don't know what you are facing",
                 "Eoin Colfer",
                 "Artemis Fowl",
                 "296 page Hardcover",
                 9749000862,
                 "Tree Publishing",
                 "One day...",
                 "Great Story",
                 [],
                 "He found something",
                 ["Fantasy", "SCI-FI"],
                 "14-Dec-01",
                 Rating,
                 200,
                 EventDiscount)

book4 = BookItem(58488,
                 "cover58488.png",
                 "Welcome to the mysterious world of god.",
                 "Cosmos",
                 "Myth of God and Inhuman",
                 "147 page Hardcover",
                 9748241734,
                 "Phailin Publishing",
                 "One day....",
                 "Interesting Book",
                 [],
                 "The god have been angered",
                 ["Fantasy", "Historical"],
                 "17-Nov-01",
                 Rating,
                 500,
                 EventDiscount)

book_one = BookItem(5566,
                   "bookcover1.png",
                   "reborn after being hit by a truck",
                   "ApeX",
                   "Reincarnation Monkey",
                   "Hard cover with 32 pages",
                   5566,
                   "Ape company",
                   "Good story",
                   [],
                   "He got hit by truck get reborn as ape",
                   ["Fantasy"],
                   "18-Mar-2023",
                   Rating,
                   777,
                   EventDiscount)

book_two = BookItem(6452,
                   "bookcover2.png",
                   "Abang selling roti",
                   "PedPro","Abang TakeOver!",
                   "Solf cover with 100 pages",
                   2546,
                   "Ape company",
                   "Exciting story",
                   [],
                   "Legendary Abang take over the world with his roti",
                   ["Cooking"],
                   "18-Mar-2023",
                   Rating(),
                   777,
                   EventDiscount())
#-------------------------------------------------------------------------------------------------------------------
#Branch

bangkok = Branch("Bangkok",
                 "6.00 - 22.00",
                 "Bangkok",
                 "0864615559",
                 "bookshop.bangkok",
                 "bangkok_bookshop",
                 [])

nonthaburi1 = Branch("Nonthaburi",
                     "8:30-22:00",
                     "Nonthaburi",
                     "0811111111",
                     "seed_nonthaburi01",
                     "NonthaburiSE-ED",
                     [])

rangsit = Branch('rangsit',
                       '9:00-23:00',
                       'future park rangsit',
                       '0983868365',
                       'bookshop.rangsit',
                       'rangsit_bookshop',
                       [])

moon_branch = Branch('Moon',
                     '23:00 - 23:59',
                     'Moon',
                     '0995471568',
                     'bookshop.moon',
                     'moon_bookshop'
                     ,[])

#-------------------------------------------------------------------------------------------------------------------
#Customer

CustomerMan = Customer("customerman@gmail.com",
                       "manmanman",
                       "Man Pokemon",
                       "Male",
                       "0899999999",
                       [],
                       "Bangkok Onnut",
                       True,
                       True)

customer1 = Customer("LLL@gmail.com", 
                      "giDruGboEEG", 
                      "Giorno Giovanna", 
                      "Male", 
                      "1234567890", 
                      [], 
                      "Nonthaburi Pakkret", 
                      False, 
                      False)

handsome_customer = Customer('petch.t1507@gmail.com',
                             '1234567890',
                             'Petch Tariyacharoen',
                             'male',
                             '089-076-7442',
                             [],
                             'prawet',
                             True,
                             True)

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
#-------------------------------------------------------------------------------------------------------------------
#Admin

AdminWoman = Admin("admingirl@gmail.com",
                   "girlgirlgirl",
                   "Girl Digimon",
                   "Female",
                   "0677777777",
                   [],
                   True)

admin1 = Admin("Admin51481@seed.ac.th",
               "AfiKfoDdvg",
               "Admin1",
               "Male",
               "0846666666",
               [],
               True)

beautiful_admin = Admin('pookantong@gmail.com',
                        '0987654321',
                        'Yotsaput Jarabekomhang',
                        'female',
                        '098-234-8731',
                        [],
                        True)

pookan_admin555 = Admin('65010895@kmitl.ac.th',
                 'PomyukmeFan55',
                 'Yotsapat',
                 'Male',
                 '0980231172',
                 [],
                 True)
#-------------------------------------------------------------------------------------------------------------------
#EventDiscount

book_lover = ("Book Lover",
              "18-Mar-23",
              "30-Mar-23",
              [],
              [],
              BookItem())
#-------------------------------------------------------------------------------------------------------------------
#EventDiscount

coupon1 = Coupon(1161,
                 "18-Dec-23",
                 10,
                 Basket())
