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
        
    def modify_book(self, new_cover, new_brief, new_creator, new_name, new_info, new_publisher, new_preview,
                    new_critic_review, new_content, new_summary, new_genre, new_date_created, new_price, new_amount):
        self._cover = new_cover
        self._brief = new_brief
        self._creator = new_creator
        self._name = new_name
        self._book_info = new_info
        self._book_publisher = new_publisher
        self._book_preview = new_preview
        self._critic_review = new_critic_review
        self._table_of_content = new_content
        self._summary = new_summary
        self._genre = new_genre
        self._date_created = new_date_created
        self._price = new_price
        self._amount_in_stock = new_amount
        
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
        self._amount = 1
        self._price = book._new_price
        
    def get_amount(self):
        return self._amount
    def set_amount(self,new_amount):
        self._amount = new_amount
    def get_name(self):
        return self._name
    def get_price(self):
        return self._price

    amount = property(get_amount,set_amount)
    name = property(get_name)
    price = property(get_price)

