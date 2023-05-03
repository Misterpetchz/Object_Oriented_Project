from Modules.Rating import Rating


class Book:
	def __init__(self, cover, brief, creator, name, book_info, book_publisher, book_preview,
				 critic_review, table_of_content, summary, genre, date_created, price, amount):
		self.__cover = cover
		self.__brief = brief
		self.__creator = creator
		self.__name = name
		self.__book_info = book_info
		self.__book_publisher = book_publisher
		self.__book_preview = book_preview
		self.__critic_review = critic_review
		self.__table_of_content = table_of_content
		self.__summary = summary
		self.__genre = genre
		self.__date_created = date_created
		self.__rating = []
		self.__price = price
		self.__amount_in_stock = amount
		self.__new_price = price
		self.__rating_score = 0

	def __repr__(self) -> str:
		return self.__name

# + Getter / Setter {START}

	@property
	def cover(self):
		return self.__cover

	@cover.setter
	def cover(self, new_cover):
		self.__cover = new_cover

	@property
	def brief(self):
		return self.__brief

	@brief.setter
	def brief(self, new_brief):
		self.__brief = new_brief

	@property
	def creator(self):
		return self.__creator

	@creator.setter
	def creator(self, new_creator):
		self.__creator = new_creator

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new_name):
		self.__name = new_name

	@property
	def book_info(self):
		return self.__book_info

	@book_info.setter
	def book_info(self, new_info):
		self.__book_info = new_info

	@property
	def book_publisher(self):
		return self.__book_publisher

	@book_publisher.setter
	def book_publisher(self, new_publisher):
		self.__book_publisher = new_publisher

	@property
	def book_preview(self):
		return self.__book_preview

	@book_preview.setter
	def book_preview(self, new_preview):
		self.__book_preview = new_preview

	@property
	def critic_review(self):
		return self.__critic_review

	@critic_review.setter
	def critic_review(self, new_critic):
		self.__critic_review = new_critic

	@property
	def table_of_content(self):
		return self.__table_of_content

	@table_of_content.setter
	def table_of_content(self, new_table):
		self.__table_of_content = new_table

	@property
	def summary(self):
		return self.__summary

	@summary.setter
	def summary(self, new_summary):
		self.__summary = new_summary

	@property
	def genre(self):
		return self.__genre

	@genre.setter
	def genre(self, new_genre):
		self.__genre = new_genre

	@property
	def date_created(self):
		return self.__date_created

	@date_created.setter
	def date_created(self, new_date):
		self.__date_created = new_date

	@property
	def rating(self):
		return self.__rating

	@rating.setter
	def rating(self, new_rating):
		self.__rating = new_rating

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, new_price):
		self.__price = new_price

	@property
	def stock_amount(self):
		return self.__amount_in_stock

	@stock_amount.setter
	def stock_amount(self, new_amount):
		self.__amount_in_stock = new_amount

	@property
	def new_price(self):
		return self.__new_price

	@new_price.setter
	def new_price(self, new_price):
		self.__new_price = new_price

	@new_price.setter
	def new_price(self, new_new_price):
		self.__new_price = new_new_price

	@property
	def rating_score(self):
		return self.__rating_score

	@rating_score.setter
	def rating_score(self, new_score):
		self.__rating_score = new_score

# + Getter / Setter {END}

# Description : Calculate new total rating score based on all rating score
	def add_rating(self, rating: Rating):
		self.__rating.append(rating)
		self.__rating_score = sum(
			[x.book_rating for x in self.__rating])/len(self.__rating)

# Description : Modify book infomation
	def modify_book(self, cover, brief, creator, name, book_info, book_publisher, book_preview,
					critic_review, table_of_content, summary, genre, date_created, price, amount):
		if isinstance(cover, str):
			if cover != '':
				self.__cover = cover
		if isinstance(brief, str):
			if brief != '':
				self.__brief = brief
		if isinstance(creator, str):
			if creator != '':
				self.__creator = creator
		if isinstance(name, str):
			if name != '':
				self.__name = name
		if isinstance(book_info, str):
			if book_info != '':
				self.__book_info = book_info
		if isinstance(book_publisher, str):
			if book_publisher != '':
				self.__book_publisher = book_publisher
		if isinstance(book_preview, str):
			if book_preview != '':
				self.__book_preview = book_preview
		if isinstance(critic_review, str):
			if critic_review != '':
				self.__critic_review = critic_review
		if isinstance(table_of_content, str):
			if table_of_content != '':
				self.__table_of_content = table_of_content
		if isinstance(summary, str):
			if summary != '':
				self.__summary = summary
		if isinstance(genre, list):
			for thing in genre:
				if thing not in self.__genre:
					self.__genre.append(genre)
			for old in self.__genre:
				if old not in genre:
					self.__genre.remove(old)
		if isinstance(date_created, str):
			if date_created != '':
				self.__date_created = date_created
		if isinstance(price, str):
			if price != '':
				self.__price = price
		if isinstance(amount, str):
			if amount != '':
				self.__amount_in_stock = amount


class BookItem(Book):
	def __init__(self, cover, brief, creator, name, book_info, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, price, amount, book_item_amount):
		super().__init__(cover, brief, creator, name, book_info, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, price, amount)
		self.__amount = book_item_amount

# + Getter / Setter {START}


	@property
	def amount(self):
		return self.__amount

	@amount.setter
	def amount(self, new_amount):
		self.__amount = new_amount
# + Getter / Setter {END}
