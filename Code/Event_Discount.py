class EventDiscount:
    def __init__(self, event_name, event_start, event_end, discounted_book, discounted_price):
        self.__event_name = event_name
        self.__event_start = event_start
        self.__event_end = event_end
        self.__discounted_book = discounted_book
        self.__discounted_price = discounted_price