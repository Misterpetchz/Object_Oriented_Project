class Order:
	def __init__(self, purchased_item, order_id, order_status,total,user):
		self._purchased_item = purchased_item
		self._order_id = order_id
		self._order_status = order_status
		self._total = total
		self._user = user

	@property
	def get_item(self):
		return self._purchased_item
	@property
	def total(self):
		return self._total
