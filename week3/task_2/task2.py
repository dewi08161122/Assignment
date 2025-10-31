# 抓取PTT資料 重點是要像一般用戶一樣抓取資料
import urllib.request as req
import bs4
# 抓取網頁 headers 內的 Request header 中的 User-Agent 
# 建立一個 request 物件, 附加 Request header 的資訊, 再利用 request 物件打開網址
def getdata(url):
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    return bs4.BeautifulSoup(data, "html.parser")

url="https://www.ptt.cc/bbs/Steam/index.html"
page=0

with open("articles.csv", "w", encoding="utf-8") as file:
    
    while page<3:
        root=getdata(url)
        titles=root.find_all("div", class_="title")
        likes=root.find_all("div", class_="nrec")

        for title, like in zip(titles, likes):
            if title.a is not None:  
                title_name=title.a.string

            if like.span is not None:
                like_count=like.span.string
            else:
                like_count=0
            
            titlelink="https://www.ptt.cc"+title.a["href"]
            actiontitle=getdata(titlelink)
            timeword=actiontitle.find("span", string="時間")
            if timeword is not None:
                time=timeword.find_next_sibling("span").text
            else:
                time=""
                
            file.write(str(title_name)+","+str(like_count)+","+str(time)+"\n")
            
        btns = root.find_all("a", class_="btn wide")
        for btn in btns:
            if "上頁" in btn.text:
                url="https://www.ptt.cc"+btn["href"]
                break
        page+=1
