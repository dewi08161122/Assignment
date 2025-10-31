// 取得JSON格式資料(陣列物件格式)
fetch("https://cwpeng.github.io/test/assignment-3-1")
.then(function(response){
    return response.json();
})
.then(function(data){
    let ndata=data.rows;
    let cdata=[]
    for(let i=0; i<ndata.length; i++){
        cdata.push({
            serial:ndata[i].serial,
            name: ndata[i].sname
        })
    }
    cdata.sort((a,b)=> a.serial - b.serial)

    fetch("https://cwpeng.github.io/test/assignment-3-2")
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        let picture=data.rows;
        let host="https://www.travel.taipei"
        let result=[]
        picture.sort((a,b)=> a.serial - b.serial)
        for(i=0; i<picture.length; i++){
            picture[i].pics=host+picture[i].pics.split(".jpg")[0]+".jpg"
        }
        for(i=0; i<cdata.length; i++){
            if(picture[i].serial==cdata[i].serial){
                result.push({
                    name: cdata[i].name,
                    picture: picture[i].pics
                })
            }
        }
        let boxes=document.querySelectorAll(".Promotion1, .Promotion2, .Promotion3");

        for (let i=0; i<3; i++){
            let box = boxes[i];
            // 清空舊內容 <div class="Promotion1">
            box.replaceChildren();
            // 新增圖片
            let img_tag=document.createElement("img"); // 建立img元素
            img_tag.setAttribute("src", result[i].picture); // 加上src標籤和img元素來源
            img_tag.classList.add("Promotionfuji"); // 加上圖片使用的CSS
            box.appendChild(img_tag); //放入圖片
            // 新增文字
            let promotion_tag=document.createElement("div"); // 建立放入文字的div
            promotion_tag.textContent=result[i].name; // 加上文字元素來源 
            promotion_tag.classList.add("Promotionword"); // 加上文字使用的CSS
            box.appendChild(promotion_tag); // 放入文字
        }
        result.splice(0,3); // 從資料result中的0開始刪除3個元素
        let box2=document.querySelectorAll(".box1")
        for (let i=0; i<10; i++){
            let box = box2[i];
            box.replaceChildren();

            let img_tag=document.createElement("img");
            img_tag.setAttribute("src", result[i].picture);
            img_tag.classList.add("boxfuji");
            box.appendChild(img_tag); 
            
            let star_tag=document.createElement("img");
            star_tag.setAttribute("src", "star.png");
            star_tag.classList.add("star");
            box.appendChild(star_tag); 

            let word_tag=document.createElement("div");
            word_tag.textContent=result[i].name;
            word_tag.classList.add("boxword");
            box.appendChild(word_tag);
        }
        result.splice(0,10);

        let loadmore = document.querySelector("#button");
        loadmore.addEventListener("click", function(){
            for (let i=0; i<10 && i < result.length; i++){
                let airbox=document.createElement("div"); // 建立一個div放入
                airbox.classList.add("box1"); 
                document.querySelector(".box").append(airbox);                
                                
                let img_tag=document.createElement("img");
                img_tag.setAttribute("src", result[i].picture);
                img_tag.classList.add("boxfuji");
                airbox.appendChild(img_tag); 
                
                let star_tag=document.createElement("img");
                star_tag.setAttribute("src", "star.png");
                star_tag.classList.add("star");
                airbox.appendChild(star_tag); 

                let word_tag=document.createElement("div");
                word_tag.textContent=result[i].name;
                word_tag.classList.add("boxword");
                airbox.appendChild(word_tag);
            }
            result.splice(0,10);
            if (result.length==0){
                loadmore.remove();
            }
        })
    });    
})
function changetomenu(){
    let phonemenudiv=document.querySelector(".phonemenu");
    phonemenudiv.style.right= "0";
}
function changetophone(){
    let phonemenudiv=document.querySelector(".phonemenu");
    phonemenudiv.style.right= "-1980px";
}