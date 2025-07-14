from instagrapi import Client

cl = Client()
cl.login("your_account", "your_password")

cl.photo_upload("E:\Fable.jpg", "Posted via Python 🐍")
