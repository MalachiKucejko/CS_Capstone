import pytest
import numpy as np
import cv2
from image_download_week1 import download_file, decode_image, resize_image, save_image


def test_download_file_success(monkeypatch):
    # Define a fake response class
    class MockResponse:
        status_code = 200
        content = b"fakebytes"

    def mock_get(url, headers):
        return MockResponse()

    # Replace requests.get with our mock
    monkeypatch.setattr("requests.get", mock_get)

    result = download_file("http://example.com", headers={})
    assert result == b"fakebytes"


def test_download_file_failure(monkeypatch):
    class MockResponse:
        status_code = 404
        content = b""

    def mock_get(url, headers):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    with pytest.raises(Exception):
        download_file("http://example.com", headers={})


def test_decode_image():
    # Create a fake 100x100 black image
    img = np.zeros((100, 100, 3), dtype=np.uint8)

    # Encode to PNG (simulate download)
    success, encoded = cv2.imencode(".png", img)
    assert success
    image_bytes = encoded.tobytes()

    # Decode with your function
    decoded = decode_image(image_bytes)
    assert decoded.shape == (100, 100, 3)
    assert decoded.dtype == np.uint8


def test_resize_image():
    # Start with a 100x100 image
    img = np.zeros((100, 100, 3), dtype=np.uint8)

    # Resize to 200x200
    resized = resize_image(img, (200, 200))
    assert resized.shape == (200, 200, 3)
    assert resized.dtype == np.uint8


def test_resize_image_downscale():
    # Start with a 200x200 image
    img = np.zeros((200, 200, 3), dtype=np.uint8)

    # Resize down to 50x50
    resized = resize_image(img, (50, 50))
    assert resized.shape == (50, 50, 3)


def test_save_image(tmp_path):
    img = np.zeros((50, 50, 3), dtype=np.uint8)
    filename = tmp_path / "test.png"

    save_image(str(filename), img)
    assert filename.exists()