class Coupon():
    def __init__(self, id, expire_date,discount_amount):
        self._id = id
        self._amount = discount_amount
        self._expire_date = expire_date
