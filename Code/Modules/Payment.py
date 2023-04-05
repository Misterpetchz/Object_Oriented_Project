import time
from promptpay import qrcode
from PIL import Image
class Payment:
    def __init__(self, amount, date, status):
        self._amount = amount
        self._date = date
        self._status = status
 
class ViaCreditCard(Payment):
    def __init__(self, amount, date, status):
        super().__init__(amount, date, status)
    def process(self):
        self._status = "paid"
        return self._status

class ViaQrCode(Payment):
    def __init__(self, amount, date, status):
        super().__init__(amount, date, status)
    def process(self):
        phone_number = "0890767442"
        payload = qrcode.generate_payload(phone_number, self._amount)
        img = qrcode.to_image(payload)
        qrcode.to_file(payload, "../qrcode-0890767442.png")
        image = Image.open("../qrcode-0890767442.png")
        image.show()
        time.sleep(3)
        self._status = 'paid'
        return self._status