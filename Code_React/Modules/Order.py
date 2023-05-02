class Order:
	def __init__(self, purchased_item, order_id, order_status, total, user):
		self.__purchased_item = purchased_item
		self.__order_id = order_id
		self.__order_status = order_status
		self.__total = total
		self.__user = user

	@property
	def get_item(self):
		return self.__purchased_item

	@property
	def total(self):
		return self.__total
