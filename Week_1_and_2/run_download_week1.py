from image_download_week1 import download_file, decode_image, resize_image, save_image

file_url = "https://tnsnapshots.com/R3_158.png"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36"
}

try:
    # Step 1: download
    file_bytes = download_file(file_url, headers)

    # Step 2: decode
    img = decode_image(file_bytes)

    # Step 3: resize
    resized_img = resize_image(img, (200, 200))

    # Step 4: save
    save_image("downloaded_file_resized.png", resized_img)

    print("File downloaded and resized to 200x200!")

except Exception as e:
    print("Error:", e)