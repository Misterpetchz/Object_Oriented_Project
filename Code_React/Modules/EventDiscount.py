from Modules.Book import Book
from datetime import datetime
import datetime


class EventDiscount():
	def __init__(self, event_name, event_start, event_end, discounted_percentage, event_genre):
		self.__event_name = event_name
		self.__event_start = event_start
		self.__event_end = event_end
		self.__discounted_percentage = discounted_percentage
		self.__event_genre = event_genre

# + Getter / Setter {START}

	@property
	def event_name(self):
		return self.__event_name

	@property
	def event_genre(self):
		return self.__event_genre

	@property
	def event_start(self):
		return self.__event_start

	@property
	def event_end(self):
		return self.__event_end

	@property
	def discounted_percentage(self):
		return self.__discounted_percentage

# + Getter / Setter {END}

# Description : Modify event
	def modify_event(self, new_name, new_start, new_end, new_percentage, new_genre):
		if isinstance(new_name, str):
			self.__event_name = new_name
		if isinstance(new_start, str):
			self.__event_start = new_start
		if isinstance(new_end, str):
			self.__event_end = new_end
		if isinstance(new_percentage, float):
			self.__discounted_percentage = new_percentage
		if isinstance(new_end, str):
			self.__event_genre = new_genre

