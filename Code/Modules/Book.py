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
    
    def get_amount_in_stock(self):
        return self._amount_in_stock
    
    def set_amount_in_stock(self,new_amount):
        self._amount_in_stock = new_amount
        
    def add_rating(self, rating:Rating):
        self._rating.append(rating)
        self._rating_score = sum([x._book_rating for x in self._rating])/len(self._rating)
         
    def modify_book(self,cover, brief, creator, name, book_info, book_publisher, book_preview, 
                 critic_review, table_of_content, summary, genre, date_created, price, amount):
        if isinstance(cover,str):
            self._cover = cover
        if isinstance(brief,str):
            self._brief = brief
        if isinstance(creator,str):
            self._creator = creator
        if isinstance(name,str):
            self._name = name
        if isinstance(book_info,str):
            self._book_info = book_info
        if isinstance(book_publisher,str):
            self._book_publisher = book_publisher
        if isinstance(book_preview,str):
            self._book_preview = book_preview
        if isinstance(critic_review,str):
            self._critic_review = critic_review
        if isinstance(table_of_content,str):
            self._table_of_content = table_of_content
        if isinstance(summary,str):
            self._summary = summary
        if isinstance(genre,str):
            self._genre = genre
        if isinstance(date_created,str):
            self._date_created = date_created
        if isinstance(price,int):
            self._price = price
        if isinstance(amount,int):
            self.amount = amount
        
    stock_amount = property(get_amount_in_stock,set_amount_in_stock)
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

