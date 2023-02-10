class Basket:
    def __init__(self, items, pay_method, coupon):
        self._items_book = items
        self.__pay_method = pay_method
        self.__coupon = coupon