import requests
import os

MARKETS = [
    ("zh-CN", "Bing-CN"),
    ("en-US", "Bing"),
    ("ja-JP", "Bing-JP"),
    ("de-DE", "Bing-DE"),
    ("en-GB", "Bing-GB")
]

RESOLUTIONS = [
    "UHD", "1920x1200", "1920x1080", "1366x768", "1280x768", 
    "1024x768", "800x600", "800x480", "768x1280", "720x1280", 
    "640x480", "480x800", "400x240", "320x240", "240x320"
]

os.makedirs("wallpapers", exist_ok=True)

for mkt, name in MARKETS:
    try:
        url = f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={mkt}"
        data = requests.get(url).json()
        base = data["images"][0]["urlbase"]
        
        for res in RESOLUTIONS:
            img_url = f"https://www.bing.com{base}_{res}.jpg"
            path = f"wallpapers/{name}_{res}.jpg"
            
            try:
                r = requests.get(img_url)
                if r.status_code == 200:
                    with open(path, "wb") as f:
                        f.write(r.content)
            except:
                pass
    except:
        pass
