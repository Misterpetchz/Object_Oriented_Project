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
        
    def add_rating(self, rating:Rating):
        self._rating.append(rating)
        self._rating_score = sum([x._book_rating for x in self._rating])/len(self._rating)
    
    def modify_book(self, data):
        if data.cover != None:
            self._cover = data.cover
        if data.brief != None:
            self._brief = data.brief
        if data.creator != None:
            self._creator = data.creator
        if data.name != None:
            self._name = data.name
        if data.book_info != None:
            self._book_info = data.book_info
        if data.book_publisher != None:
            self._book_publisher = data.book_publisher
        if data.book_preview != None:
            self._book_preview = data.book_preview
        if data.critic_review != None:
            self._critic_review = data.critic_review
        if data.table_of_content != None:
            self._table_of_content = data.table_of_content
        if data.summary != None:
            self._summary = data.summary
        if data.genre != None:
            self.delete_list = []
            for i in range(len(data.genre)):
                if data.genre[i] not in self._genre:
                    if data.genre[i][0] != '-':
                        self._genre.append(data.genre[i])
                    if data.genre[i][1:] in self._genre:
                        self._genre.remove(data.genre[i][1:])
        if data.date_created != None:
            self._date_created = data.date_created
        if data.price != None:
            self._price = data.price
        if data.amount != None:
            self._amount_in_stock = data.amount
        
    
        
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
   


