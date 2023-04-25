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

    @property
    def status(self):
        return self.__status

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

    @property
    def qr(self):
        return self.__qr

    @property
    def status(self):
        return self.__status

    def generate_qr_code(self):
        promptpay_number = "0890767442"
        payload = qrcode.generate_payload(promptpay_number, self._amount)
        img = qrcode.to_image(payload)
        buffered = BytesIO()
        img.save(buffered, format='PNG')
        img_bytes = buffered.getvalue()
        self.__qr = base64.b64encode(img_bytes).decode('utf-8')
        # self.__qr = base64.b64encode(qr_image_data)

        print(self.__qr)
        return self.__qr

    def check_status(self, status):
        if status.lower() == 'paid':
            self.__status = 'paid'
            # return self.__status
        else:
            self.__status = 'reject'
            # return self.__status