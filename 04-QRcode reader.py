#Read-QRcode
from qrtools import QR
my_QR = QR(filename = ".png")
my_QR.decode()
print(my_QR.data)
