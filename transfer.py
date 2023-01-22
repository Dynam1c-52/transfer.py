import requests
import webbrowser

loc = input("Enter file name: ")
transfer = "https://transfer.sh/"
with open(loc, "rb") as f:
    up = {"file": (f)}
    req = requests.post(transfer, files=up)
link = req.text
print('---------------------------------')
print("There is your url:\n" + link)
webbrowser.open(link)