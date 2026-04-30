import requests

video_url = "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"

response = requests.get(video_url, stream=True)

response.raise_for_status()

downloaded = 0

with open("/media/shadyahmed/C69EBC679EBC5223/Users/ECC.DESKTOP-BOGB7O8/Desktop/reading/ReadingComputerScience/chapters/chapter 12_WebScraping/videodownloaded.mp4", "wb") as video_file:
    for chunk in response.iter_content(1024 * 1024):

        if chunk:
            video_file.write(chunk)

            downloaded += len(chunk)

            print(f"Downloaded: {downloaded / (1024 * 1024):.2f} MB")

print("Download complete ✅")