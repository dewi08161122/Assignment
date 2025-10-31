import urllib.request as req
import json
urlch="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
urlen="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
with req.urlopen(urlch) as response:
    datach=json.load(response) #利用json的模組處理json的資料格式
with req.urlopen(urlen) as response:
    dataen=json.load(response)
clistch=datach["list"]
clisten=dataen["list"]
with open("hotels.csv", "w", encoding="utf-8") as file:
    for ch,en in zip(clistch,clisten):
        file.write(ch["旅宿名稱"]+","+en["hotel name"]+","+ch["地址"]+","+en["address"]+","+ch["電話或手機號碼"]+","+ch["傳真"]+","+ch["房間數"]+"\n")

tpa={}
for number in clistch:
    if "區" in number["地址"]:
        area=number["地址"].split("區")[0].replace("臺北市","")+"區"
    room= int(number["房間數"])
    if area not in tpa:
        tpa[area]={"hotel":0, "room":0}        
    tpa[area]["hotel"]+=1
    tpa[area]["room"]+=room

all=[]
for area, data in tpa.items():
    all.append({"area": area, "hotel": data["hotel"], "room": data["room"]})


with open("districts.csv", "w", encoding="utf-8") as file:
    for tpaarea in all:
        file.write(tpaarea["area"] + "," + str(tpaarea["hotel"]) + "," + str(tpaarea["room"]) + "\n")

