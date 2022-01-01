#Code by Eitan Biletski - TEnLOcODE 2022

import requests #pip install requests
from PIL import Image #pip install pillow
import json #comes with python

username = input("Minecraft Username: ") #asking username
s = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username, verify=True) #s var
r = json.loads(s.text) #r var
uuid = r["id"] #uuid var
print(username + "'s UUID: " + uuid) #prints usernames uuid
print("URL ASSETS") #prints "URL ASSETS"
w1 = "https://crafatar.com/renders/body/" + uuid #w1 var
w2 = "https://crafatar.com/renders/body/" + uuid + "?overlay=true" #w2 var
w3 = "https://crafatar.com/skins/" + uuid #w3 var
print(w1) #prints w1 var value
print(w2) #prints w2 var value
print(w3) #prints w3 var value
print("\n\n") #prints space
c1 = Image.open(requests.get(w1, stream=True).raw) #c1 var
c2 = Image.open(requests.get(w2, stream=True).raw) #c2 var
c3 = Image.open(requests.get(w3, stream=True).raw) #c3 var
print("Saving Images..") #prints "Saving Images..."
c1.save("body.png") #saving img c1
c2.save("bodywo.png") #saving img c2
c3.save("fullskin.png") #saving img c3
print("Saved!") #prints "Saved!"
print("body.png - 3D body") #desc
print("bodywo.png - 3D body with overlay (jackets, hats & silm skin)") #desc
print("fullskin.png - Skin Template") #desc
