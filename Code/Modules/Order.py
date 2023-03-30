class Order:
    def __init__(self, purchased_item, order_id, order_status,payment,user):
        self._purchased_item = purchased_item
        self._order_id = order_id
        self._order_status = order_status
        self._payment = payment
        self._user = user

    def get_list_of_book_item (self, Basket):
        pass