class Payment:
<<<<<<< HEAD
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
    
=======
    def __init__(self, amount, order_id, date, status):
        self.amount = amount
        self.order_id = order_id
        self.date = date
        self.status = status

class CreditCard(Payment):
    def __init__(self, amount, order_id, date, status, card_num, expire_card, cvc):
        super().__init__(amount, order_id, date, status)
        self.card_name = card_num
        self.expire_card = expire_card
        self.cvc = cvc
        
class Bank(Payment):
    def __init__(self, amount, order_id, date, status):
        super().__init__(amount, order_id, date, status)
        pass

class cash(Payment):
    def __init__(self, amount, order_id, date, status):
        super().__init__(amount, order_id, date, status)
>>>>>>> f28697a92b79e001dffb0a48c5cdcc6f2930c7ae
