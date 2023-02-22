class Book : 
    def __init__(self, product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, 
                 critic_review, table_of_content, summary, genre, date_created, rating):
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
class BookItem(Book):
    def __init__(self, product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, event_discount):
        super().__init__(product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating)
        