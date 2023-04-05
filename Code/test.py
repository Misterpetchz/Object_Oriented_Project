from Modules.Payment import ViaQrCode

pay = ViaQrCode(1000,"15-07-2004","Not-paid")
print(pay.process())