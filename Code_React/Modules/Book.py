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
    ##################################################################################################################
        #GETTER/SETTER#
    @property
    def stock_amount(self):
        return self._amount_in_stock
    @stock_amount.setter
    def stock_amount(self,new_amount):
        self._amount_in_stock = new_amount
    ##################################################################################################################
    def add_rating(self, rating:Rating):
        self._rating.append(rating)
        self._rating_score = sum([x._book_rating for x in self._rating])/len(self._rating)
         
    def modify_book(self,cover, brief, creator, name, book_info, book_publisher, book_preview, 
                 critic_review, table_of_content, summary, genre, date_created, price, amount):
        if isinstance(cover,str):
            if cover != '':
                self._cover = cover
        if isinstance(brief,str):
            if brief != '':
                self._brief = brief
        if isinstance(creator,str):
            if creator != '':
                self._creator = creator
        if isinstance(name,str):
            if name != '':
                self._name = name
        if isinstance(book_info,str):
            if book_info != '':
                self._book_info = book_info
        if isinstance(book_publisher,str):
            if book_publisher != '':
                self._book_publisher = book_publisher
        if isinstance(book_preview,str):
            if book_preview != '':
                self._book_preview = book_preview
        if isinstance(critic_review,str):
            if critic_review != '':
                self._critic_review = critic_review
        if isinstance(table_of_content,str):
            if table_of_content != '':
                self._table_of_content = table_of_content
        if isinstance(summary,str):
            if summary != '':
                self._summary = summary
        if isinstance(genre, list):
            for thing in genre:
                if thing not in self._genre:
                    self._genre.append(genre)
            for old in self._genre:
                if old not in genre:
                    self._genre.remove(old)
        if isinstance(date_created,str):
            if date_created != '':
                self._date_created = date_created
        if isinstance(price,str):
            if price != '':
                self._price = price
        if isinstance(amount,str):
            if amount != '':
                self.amount = amount
        
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
        
    #################################################################################################################
        #GETTER/SETTER#
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,new_amount):
        self._amount = new_amount
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    ################################################################################################################

