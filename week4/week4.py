from fastapi import FastAPI, Path, Query, Body, Form, Request
from fastapi.responses import FileResponse, RedirectResponse  # 回應檔案內容
from typing import Annotated  # 協助資料型態驗證
from fastapi.staticfiles import StaticFiles  # 統一處理靜態檔案
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware # 用來做簽章
app=FastAPI() # FastAPI物件
app.add_middleware(SessionMiddleware,secret_key="1111")
templates = Jinja2Templates(directory="templates") # 指定HTML模板資料夾

@app.post("/login")
def login(email: Annotated[str, Form()], password: Annotated[str, Form()], request: Request):
    if email =="abc@abc.com" and password =="123":
        request.session["user"]=email
        return RedirectResponse(url="/member", status_code=303)
    elif email =="" and password =="":
        msg = "請輸入信箱和密碼"
        return RedirectResponse(url="/ohoh?msg="+msg, status_code=303)
    elif email !="abc@abc.com" and password =="123":
        msg = "信箱輸⼊錯誤"
        return RedirectResponse(url="/ohoh?msg="+msg, status_code=303)
    elif email =="abc@abc.com" and password !="123":
        msg = "密碼輸⼊錯誤"
        return RedirectResponse(url="/ohoh?msg="+msg, status_code=303)
    else:
        msg = "信箱、密碼輸⼊錯誤"
        return RedirectResponse(url="/ohoh?msg="+msg, status_code=303)

@app.get("/logout")
def logout(request: Request):
    request.session.clear() # 清除後端的紀錄
    response = RedirectResponse("/", status_code=303)
    response.delete_cookie("session")  # 告訴瀏覽器刪除名為 session 的 cookie(刪除前端的紀錄)
    return response

@app.get("/member")
def member(request: Request):
    if "user" in request.session:
        return FileResponse("templates/member.html")
    else:
        return RedirectResponse("/")

@app.get("/ohoh")
def ohoh(request: Request, msg):
    return templates.TemplateResponse("ohoh.html", {"request": request, "msg": msg})

import urllib.request as req
import json
urlch="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
urlen="https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
with req.urlopen(urlch) as response:
    datach=json.load(response) 
with req.urlopen(urlen) as response:
    dataen=json.load(response)

clistch=sorted(datach["list"], key=lambda x:x["_id"])
clisten=sorted(dataen["list"], key=lambda x:x["_id"])
hotellist={}
i=1
for ch,en in zip(clistch,clisten):
    hotellist[i] = ch["旅宿名稱"] + "、" + en["hotel name"] + "、" + ch["電話或手機號碼"]
    i+=1

@app.get("/hotel/{hotel_id}")
def hotel(request: Request, hotel_id: int):
    if hotel_id in hotellist:
        msg = hotellist[hotel_id]
        return templates.TemplateResponse("hotel.html", {"request": request, "msg": msg})
    else:
        msg = "查詢不到相關資料"
        return templates.TemplateResponse("hotel.html", {"request": request, "msg": msg})


# 靜態檔案處理放在最下方
app.mount("/static", StaticFiles(directory="static"), name="static")  # 中取對應資料夾內的CSS
app.mount("/", StaticFiles(directory="templates", html=True))  # html=True會自動讀取名稱為index的html為首頁

