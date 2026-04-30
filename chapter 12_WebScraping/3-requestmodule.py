import requests, sys, webbrowser, pyperclip
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
print(res.status_code == requests.codes.ok)
print(res.status_code)
print(len(res.text))
178981
print(res.text[:248])
#webbrowser.open('https://automatetheboringstuff.com/files/rj.txt')