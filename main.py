import requests
import os

BASE_URL = "https://www.bing.com"
API_URL = "https://www.bing.com/HPImageArchive.aspx"
SAVE_DIR = "."

MARKETS = [
    ("zh-CN", "Bing-CN"),
    ("en-US", "Bing"),
    ("ja-JP", "Bing-JP"),
    ("de-DE", "Bing-DE"),
    ("en-GB", "Bing-GB")
]

RESOLUTIONS = [
    "UHD",
    "1920x1200",
    "1920x1080",
    "1366x768",
    "1280x768",
    "1024x768",
    "800x600",
    "800x480",
    "768x1280",
    "720x1280",
    "640x480",
    "480x800"
]

def download_images():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for mkt_code, prefix in MARKETS:
        try:
            params = {
                "format": "js",
                "idx": 0,
                "n": 1,
                "mkt": mkt_code
            }
            resp = requests.get(API_URL, params=params, headers=headers).json()
            
            if not resp.get("images"):
                continue

            image_data = resp["images"][0]
            urlbase = image_data["urlbase"]
            
            if not urlbase.startswith("http"):
                urlbase = BASE_URL + urlbase

            for res in RESOLUTIONS:
                img_url = f"{urlbase}_{res}.jpg"
                filename = f"{prefix}-{res}.jpg"
                path = os.path.join(SAVE_DIR, filename)

                try:
                    img_resp = requests.get(img_url, headers=headers, stream=True)
                    if img_resp.status_code == 200:
                        with open(path, "wb") as f:
                            for chunk in img_resp.iter_content(1024):
                                f.write(chunk)
                except Exception:
                    pass

        except Exception:
            pass

if __name__ == "__main__":
    download_images()
