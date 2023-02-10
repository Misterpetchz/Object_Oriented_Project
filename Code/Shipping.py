class Shipping:
    def __init__(self, purchased_item, order_id, shipping_status,payment):
        self._purchased_item = purchased_item
        self._order_id = order_id
        self._shipping_status = shipping_status
        self._payment = payment
