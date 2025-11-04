from pyzxing import BarCodeReader
reader = BarCodeReader()
result = reader.decode("ticket_qr.png")     # or a directory
print(result)