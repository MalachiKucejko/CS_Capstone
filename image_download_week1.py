import requests
import cv2
import numpy as np


def download_file(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")


def decode_image(image_bytes):
    img_array = np.frombuffer(image_bytes, np.uint8)
    return cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)


def resize_image(img, size=(200, 200)):
    return cv2.resize(img, size)


def save_image(filename, img):
    cv2.imwrite(filename, img)
