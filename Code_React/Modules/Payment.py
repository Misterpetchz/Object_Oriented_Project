import time
from promptpay import qrcode
from qrcode import QRCode, make
import base64
from Modules.settings import *
from io import BytesIO


class Payment:
	def __init__(self, amount, date):
		self._amount = amount
		self._date = date


class ViaCreditCard(Payment):
	def __init__(self, amount, date):
		super().__init__(amount, date)
		self.__status = None

# + Getter / Setter {START}

	@property
	def status(self):
		return self.__status

# + Getter / Setter {END}

# Description : Check payment status of the the check (pseudo function)
	def check_status(self, status):
		if status == 'paid':
			self.__status = 'paid'
		else:
			self.__status = 'reject'


class ViaQrCode(Payment):
	def __init__(self, amount, date):
		super().__init__(amount, date)
		self.__status = None
		self.__qr = None

# + Getter / Setter {START}

	@property
	def qr(self):
		return self.__qr

	@property
	def status(self):
		return self.__status

# + Getter / Setter {END}

# Description : print qrcode image from base64
	def generate_qr_code(self):
		promptpay_number = "0890767442"
		payload = qrcode.generate_payload(promptpay_number, self._amount)
		img = qrcode.to_image(payload)
		buffered = BytesIO()
		img.save(buffered, format='PNG')
		img_bytes = buffered.getvalue()
		self.__qr = base64.b64encode(img_bytes).decode('utf-8')
		return self.__qr

# Description : Check payment status of the the check (pseudo function)
	def check_status(self, status):
		if status.lower() == 'paid':
			self.__status = 'paid'
		else:
			self.__status = 'reject'
