import sys
import numpy as np
from PIL import Image
import re
import cv2

def encode(message, path):
    # Encode message into 8-bit binary
    b_message = ''.join(["{:08b}".format(ord(x)) for x in message])
    b_message = np.array([int(x) for x in b_message], dtype=np.uint8)

    b_message_length = len(b_message)

    # Open image
    with Image.open("uff.png") as img:
        width, height = img.size
        data = np.array(img)

    # Flatten image array
    data = data.flatten()

    # Check if message fits
    if b_message_length > len(data):
        raise ValueError("Message is too large for this image.")

    # Overwrite LSB
    data[:b_message_length] = (data[:b_message_length] & 0xFE) | b_message

    # Reshape back
    data = data.reshape((height, width, 3))

    # Save new image
    new_img = Image.fromarray(data)
    new_img.save(f"steg_img.png")
    new_img.show()

def decode(path):

    with Image.open(path) as img:
        width, height = img.size
        img_format = img.format
        data = np.array(img)

    if img_format == "JPEG":
        gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        h, w = gray.shape

        dct_blocks = []

        for i in range(0, h - 8, 8):
            for j in range(0, w - 8, 8):
                block = gray[i:i + 8, j:j + 8]
                dct = cv2.dct(np.float32(block))
                dct_blocks.append(dct)

        dct_blocks = np.array(dct_blocks)

        # Ignore DC coefficient
        mid_freq = dct_blocks[:, 2:6, 2:6]

        variance = np.var(mid_freq)

        if variance > 20:  # empirical threshold
            return "Suspicious! Possible JPEG steganography (J-UNIWARD / JMiPOD / UERD)"
        else:
            return "Safe!"

    else:
        data = np.reshape(data, width * height * 3)

        # Extract LSB
        data = data & 1

        # Convert bits → bytes
        data = np.packbits(data)

        message = ""

        for x in data:
            char = chr(x)
            if not char.isprintable():
                break
            message += char

        # --- Meaningful Text Check ---
        # Looks for 4+ consecutive alphabets
        if re.search(r'[A-Za-z]{4,}', message):
            return "Suspicious! Might contain hidden embeddings"
        else:
            return "Safe!"

result = decode("Safe1-secret.png")
