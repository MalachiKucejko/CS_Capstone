import requests
import cv2
import numpy as np

# Download the file
file_url = "https://tnsnapshots.com/R3_158.png"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(file_url, headers=headers)

if response.status_code == 200:
    # Convert image bytes to NumPy array
    img_array = np.frombuffer(response.content, np.uint8)
    
    # Decode image
    img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)
    
    # Resize to 200x200
    resized_img = cv2.resize(img, (200, 200))
    
    # Save resized image
    cv2.imwrite("downloaded_file_resized.png", resized_img)
    
    print("File downloaded and resized to 200x200!")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
