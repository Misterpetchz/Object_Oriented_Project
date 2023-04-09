import time
from promptpay import qrcode


class Payment:
    def __init__(self, amount, date):
        self._amount = amount
        self._date = date
 
class ViaCreditCard(Payment):
    def __init__(self, amount, date):
        super().__init__(amount, date)

class ViaQrCode(Payment):
    def __init__(self, amount, date):
        super().__init__(amount, date)

    def generate_qr_code(self):
        promptpay_number = "0890767442"
        payload = qrcode.generate_payload(promptpay_number, self._amount)
        qrcode.to_file(payload, "../qrcode-0890767442.png")
