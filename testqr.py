from promptpay import qrcode

# generate a payload
id_or_phone_number = "0980231172"
payload = qrcode.generate_payload(id_or_phone_number)
payload_with_amount = qrcode.generate_payload(id_or_phone_number, 100)

# export to PIL image
img = qrcode.to_image(payload)

# export to file
qrcode.to_file(payload_with_amount, "./qrcode-0890767442.png") 