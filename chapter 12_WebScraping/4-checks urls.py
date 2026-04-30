import requests
from pathlib import Path

address = ""
if len(sys.argv) != 0:
    # Get address from command line.
    address = sys.argv[0]
else:
    # Get address from clipboard.
    address = pyperclip.paste()
path = Path(address)
with open(path, "r") as file:

    
    for line in file:

    
        url = line.strip()

        if not url:
            continue
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        try:
            # إرسال Request
            response = requests.get(url)

            # طباعة الـ status code
            print(f"{url} --> {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"{url} --> ERROR: {e}")