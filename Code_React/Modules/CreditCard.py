from typing import Optional
class CreditCard:
    def __init__(self, card_num:int = None, expire_date:int = None, cvc:int = None):
        self.__card_num = card_num
        self.__expire_date = expire_date
        self.__cvc = cvc

    ##################################################################################################################
        #GETTER/SETTER
    @property
    def card_num(self):
        return self.__card_num
    @card_num.setter
    def card_num(self, new_card_num):
         self.__card_num = new_card_num
    @property
    def expire_date(self):
        return self.__expire_date
    @expire_date.setter
    def expire_date(self, new_expire_date):
        self.__expire_date = new_expire_date
    @property
    def cvc(self):
        return self.__cvc
    @cvc.setter
    def cvc(self, new_cvc):
        self.__cvc = new_cvc

    ##################################################################################################################
    def modify_credit_card_info(self, new_card_num, new_expire_date, new_cvc):
        if isinstance(new_card_num, str):
            self.card_num = new_card_num
        if isinstance(new_expire_date, str):
            self.expire_date = new_expire_date
        if isinstance(new_cvc, str):
            self.cvc = new_cvc
