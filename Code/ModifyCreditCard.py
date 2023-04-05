from Modules.CreditCard import CreditCard
from Modules.UserAccount import Customer

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

pookanCard = CreditCard('02131284',
                        '12-02-23',
                        '0212')
pookanCard.modify_credit_card_info("012321",
                                   "12-02-25",
                                   '01232')
print(pookanCard.cvc)