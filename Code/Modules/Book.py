from Modules.Rating import Rating
class Book : 
    def __init__(self, cover, brief, creator, name, book_info, book_publisher, book_preview, 
                 critic_review, table_of_content, summary, genre, date_created, price, amount):
        self._cover = cover
        self._brief = brief
        self._creator = creator
        self._name = name
        self._book_info = book_info
        self._book_publisher = book_publisher
        self._book_preview = book_preview
        self._critic_review = critic_review
        self._table_of_content = table_of_content
        self._summary = summary
        self._genre = genre
        self._date_created = date_created
        self._rating = []
        self._price = price
        self._amount_in_stock = amount
        self._new_price = price
        self._rating_score = 0
    
    def __repr__(self) -> str:
        return self._name
        
    def add_rating(self, rating:Rating):
        self._rating.append(rating)
        self._rating_score = sum([x._book_rating for x in self._rating])/len(self._rating)
        
    
        
#class BookItem():
   # def __init__(self, cover, creator, name, book_info, genre, date_created, price):
        

class BookItem():
    def __init__(self, book):
        self._cover = book._cover
        self._creator = book._creator
        self._name = book._name
        self._book_info = book._book_info
        self._genre = book._genre
        self._date_created = book._date_created
        self._price = book._new_price
   


