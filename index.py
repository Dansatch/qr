import cv2
from pyzbar.pyzbar import decode

# Replace with your ticket QR/Aztec image path
image_path = './aztec_code.png'

# Load image
img = cv2.imread(image_path)

# Decode all barcodes/QR/Aztec codes in the image
decoded_objects = decode(img)

if not decoded_objects:
    print("No barcode/QR/Aztec code detected. Try adjusting image contrast or resolution.")
else:
    for obj in decoded_objects:
        print(f"Type: {obj.type}")
        raw_data = obj.data
        print(f"Raw bytes: {raw_data}")
        print(f"Hex: {raw_data.hex()}")
        try:
            print(f"Text (if readable): {raw_data.decode('utf-8')}")
        except UnicodeDecodeError:
            print("Text: Not valid UTF-8")
