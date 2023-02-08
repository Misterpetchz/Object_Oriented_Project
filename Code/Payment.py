class Payment:
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

class Cash(Payment):
    def __init__(self, amount, order_id, date, status):
        super().__init__(amount, order_id, date, status)
        pass