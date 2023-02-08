class Book : 
    def __init__(self, product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, 
                 critic_review, table_of_content, summary, genre, date_created) :
        self.__product_id = product_id
        self.__cover = cover
        self.__brief = brief
        self.__creator = creator
        self.__name = name
        self.__book_info = book_info
        self.__book_ISBN_id = book_ISBN_id
        self.__book_publisher = book_publisher
        self.__book_preview = book_preview
        self.__critic_review = critic_review
        self.__table_of_content = table_of_content
        self.__summary = summary
        self.__genre = genre
        self.__date_created = date_created 
