# 先資料庫連線
import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="11221122",
    host="localhost",
    database="fastapi"
)
print("Database Ready")

from fastapi import FastAPI, Body, Request
from fastapi.responses import FileResponse, RedirectResponse  # 回應檔案內容
from typing import Annotated  # 協助資料型態驗證
from fastapi.staticfiles import StaticFiles  # 統一處理靜態檔案
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware # 用來做簽章
import json
app=FastAPI()
app.add_middleware(SessionMiddleware,secret_key="1111") # 管理使用者狀態
templates = Jinja2Templates(directory="public")

@app.post("/signup")
def signup(body=Body(None)):
    body=json.loads(body) # 用json格式解讀body資料
    name=body["name"]
    email=body["email"]
    password=body["password"]
    # 檢查email是否重複(從mysql抓取資料比對)
    cursor=con.cursor()
    cursor.execute("SELECT * FROM member WHERE email=%s",[email])
    result=cursor.fetchone() # 抓取一筆資料
    if result==None:
        cursor.execute("INSERT INTO member(name,email,password) VALUES(%s,%s,%s)",[name, email, password])
        con.commit()
        return{"ok":True}
    else:
        return{"ok":False}

@app.post("/login")
def login(request: Request, body=Body(None)):
    body=json.loads(body)
    email=body["email"]
    password=body["password"]
    cursor=con.cursor()
    cursor.execute("SELECT * FROM member WHERE email=%s",[email])
    result=cursor.fetchone()
    if result==None:
        request.session["member"]=None
        return{"email":True}
    elif result[3]!=password:
        request.session["member"]=None
        return{"password":True}
    else:
        request.session["member"]={
            "name":result[1], "email":result[2]
        }
        return{"ok":True}

@app.get("/logout")
def logout(request: Request):
    request.session["member"]=None
    response = RedirectResponse("/", status_code=303)
    return response

@app.get("/cheak")
def check_status(request: Request):
    if "member" in request.session and request.session["member"]!=None:
        return{"ok":True,}
    else:
        return{"ok":False}
    
@app.get("/member")
def member(request: Request):
    if "member" in request.session:
        cursor=con.cursor(dictionary=True) # 會用字典的形式把資料取出
        cursor.execute("SELECT * FROM message")
        messages=cursor.fetchall()
        name=request.session["member"]
        return templates.TemplateResponse("member.html", {
            "request": request, "name":name["name"], "messages": messages})
    else:
        return RedirectResponse("/")

@app.get("/ohoh")
def ohoh(request: Request, msg):
    return templates.TemplateResponse("ohoh.html", {"request": request, "msg": msg})
    
@app.post("/createMessage")
def createmessage(request: Request, body=Body(None)):
    body=json.loads(body)
    member=request.session["member"]
    author=member["name"]
    content=body["content"]
    cursor=con.cursor()
    cursor.execute("INSERT INTO message(author,content) VALUES(%s,%s)",[author, content])
    con.commit()
    return{"ok":True}

@app.get("/getMessage")
def getmessage():
    cursor=con.cursor(dictionary=True) # 會用字典的形式把資料取出
    cursor.execute("SELECT * FROM message")
    data=cursor.fetchall()
    return data

@app.post("/deleteMessage")
def deletemessage(body=Body(None)):
    body=json.loads(body)
    id=body["id"]
    cursor=con.cursor()
    cursor.execute("DELETE FROM message WHERE id=%s", [id])
    con.commit()
    return{"ok":True}


# 靜態檔案處理放在最下方
app.mount("/static", StaticFiles(directory="static"), name="static")  # 中取對應資料夾內的CSS
app.mount("/", StaticFiles(directory="public", html=True))  # html=True會自動讀取名稱為index的html為首頁
