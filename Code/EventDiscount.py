class EventDiscount():
    def __init__(self, event_name, event_start, event_end, discounted_book, discounted_price):
        self._event_name = event_name
        self._event_start = event_start
        self._event_end = event_end
        self._discounted_book = discounted_book
        self._discounted_price = discounted_price
