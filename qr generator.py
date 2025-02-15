#qr generator
# import module

import pyqrcode

print("Welcome to QR code generator")

msg = input("Type your secret message: ")

code = pyqrcode.create(msg)

code.png("QRCODE.png",scale = 5)

print("QR code generated successfully !")