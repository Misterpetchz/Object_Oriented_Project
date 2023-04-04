from Modules.Rating import Rating
class Book : 
    def __init__(self, product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, 
                 critic_review, table_of_content, summary, genre, date_created, rating, price):
        self._product_id = product_id
        self._cover = cover
        self._brief = brief
        self._creator = creator
        self._name = name
        self._book_info = book_info
        self._book_ISBN_id = book_ISBN_id
        self._book_publisher = book_publisher
        self._book_preview = book_preview
        self._critic_review = critic_review
        self._table_of_content = table_of_content
        self._summary = summary
        self._genre = genre
        self._date_created = date_created
        self._rating = rating
        self._price = price
    def add_rating(self, rating:Rating):
        self._rating.append(rating)

class BookItem(Book):
    def __init__(self, product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, price, event_discount):
        super().__init__(product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, price)
        self.__event_discount = event_discount
        
    def get_branch_with_book(Book):
        pass
    
    def get_event_discount(self):
        return self.__event_discount
    
    def set_event_discount(self, new_event_discount):
        self.__event_discount = new_event_discount

 

    event_discount = property(get_event_discount,set_event_discount)