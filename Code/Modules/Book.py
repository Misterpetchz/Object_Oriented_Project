class Book : 
    def __init__(self, cover, brief, creator, name, book_info, book_publisher, book_preview, 
                 critic_review, table_of_content, summary, genre, date_created, rating, price, amount):
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
        self._rating = rating
        self._price = price
        self._amount_in_stock = amount
        self._new_price = price
class BookItem(Book):
    def __init__(self, book):
        super().__init__(book._cover, book._brief, book._creator, book._name, book._book_info, book._book_publisher, book._book._book_preview, book._critic_review, book._table_of_content, book._summary, book._genre, book._date_created, book._rating, book._price)
    def get_branch_with_book(Book):
        pass
'''  
class test(Book):
    def __init__(self, book):
        super().__init__(diction['cover'], brief, creator, name, book_info, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, book., amount)
'''