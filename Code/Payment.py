class Payment:
    def __init__(self, amount, date):
        self._amount = amount
        self._date = date

class QrPayment(Payment):
    def __init__(self, amount, date, brief):
        super().__init__(amount, date)
        self._brief = brief

class CreditCard(Payment):
    def __init__(self, amount, date, card_num, expire_date, cvc):
        super().__init__(amount, date)
        self.__card_num = card_num
        self.__expire_dare = expire_date
        self.__cvc = cvc
