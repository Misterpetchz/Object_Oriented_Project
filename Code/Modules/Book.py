class Book : 
    def __init__(self, cover, brief, creator, name, book_info, book_publisher, book_preview, 
                 critic_review, table_of_content, summary, genre, date_created, rating, price, amount):
        #self._product_id = product_id
        self._cover = cover
        self._brief = brief
        self._creator = creator
        self._name = name
        self._book_info = book_info
        #self._book_ISBN_id = book_ISBN_id
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
class BookItem(Book):
    def __init__(self, cover, brief, creator, name, book_info, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, price, book_ISBN_id):
        super().__init__(cover, brief, creator, name, book_info, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, price, 'unvalue')
        self._book_ISBN_id = book_ISBN_id
    def get_branch_with_book(Book):
        pass
