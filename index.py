import PIL.Image
# import pyzbar 
# import PIL
import pyzbar.pyzbar

# Replace 'ticket_qr.png' with the path to your QR code image
image_path = './qr2.png'
image = PIL.Image.open(image_path)

# Decode the QR code
decoded_objects = pyzbar.pyzbar.decode(image)

if decoded_objects:
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data (raw):", obj.data)
        print("Data (decoded text if possible):", obj.data.decode('utf-8', errors='ignore'))
else:
    print("No QR code detected in the image.")
