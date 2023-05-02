class Rating:
	def __init__(self, book_rating, book_comment, user):
		self.__book_rating = book_rating
		self.__book_comment = book_comment
		self.__user = user

	@property
	def book_rating(self):
		return self.__book_rating

	@property
	def book_comment(self):
		return self.__book_comment

	@property
	def user(self):
		return self.__user
