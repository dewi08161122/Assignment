console.log("=== Task 1 ===")
function func1(name){ 
const place=[ 
{"id":"悟空", "x":0, "y":0}, 
{"id":"辛巴", "x":-3, "y":3}, 
{"id":"貝吉塔", "x":-4, "y":-1},
{"id":"特南克斯", "x":1, "y":-2}, 
{"id":"丁滿", "x":-1, "y":4}, 
{"id":"弗利沙", "x":4, "y":-1}, 
]
let me=[]
let distance=[]
let yyy=[]
let zzz=[]

for(let i=0; i<place.length; i++){
    if(name == place[i].id){
        me.push(place[i].x);
        me.push(place[i].y);
    }
}

if(name=="悟空" || name=="辛巴" || name=="貝吉塔" || name=="特南克斯"){
    for(i=0; i<place.length; i++){
        let dx=Number(me[0])-Number(place[i].x)
        let dy=Number(me[1])-Number(place[i].y)
        let z=Math.abs(dx)+Math.abs(dy)
        if(place[i].id=="丁滿" || place[i].id=="弗利沙"){
            z+=2;
        }
        if(z>0){
            distance.push(z)
        }
    }
    let closest=Math.min(...distance)
    let farest=Math.max(...distance)
    for(i=0; i<place.length; i++){
        let dx=Number(me[0])-Number(place[i].x)
        let dy=Number(me[1])-Number(place[i].y)
        let z=Math.abs(dx)+Math.abs(dy)
        if(place[i].id=="丁滿" || place[i].id=="弗利沙"){
            z+=2;
        }
        if (z==closest){
            yyy.push(place[i].id)
        }else if(z==farest){
            zzz.push(place[i].id)
        }
    }
}else if(name=="丁滿" || name=="弗利沙"){
    for(i=0; i<place.length; i++){
        let dx=Number(me[0])-Number(place[i].x)
        let dy=Number(me[1])-Number(place[i].y)
        let z=Math.abs(dx)+Math.abs(dy)
        if(place[i].id=="悟空" || place[i].id=="辛巴"|| place[i].id=="貝吉塔"|| place[i].id=="特南克斯"){
            z+=2;
        }
        if(z>0){
            distance.push(z)
        }
    }
    let closest=Math.min(...distance)
    let farest=Math.max(...distance)
    for(i=0; i<place.length; i++){
        let dx=Number(me[0])-Number(place[i].x)
        let dy=Number(me[1])-Number(place[i].y)
        let z=Math.abs(dx)+Math.abs(dy)
        if(place[i].id=="悟空" || place[i].id=="辛巴"|| place[i].id=="貝吉塔"|| place[i].id=="特南克斯"){
            z+=2;
        }
        if (z==closest){
            yyy.push(place[i].id)
        }else if(z==farest){
            zzz.push(place[i].id)
        }
    }
}
if(yyy.length==1 && zzz.length==1){
    console.log(`最遠${zzz}，最近${yyy}`)
}else{
    console.log(`最遠${zzz.join("、")}；最近${yyy.join("、")}`);
}
}
func1("辛巴");  // print 最遠弗利沙；最近丁滿、⾙吉塔
func1("悟空");  // print 最遠丁滿、弗利沙；最近特南克斯
func1("弗利沙");  // print 最遠⾟巴，最近特南克斯
func1("特南克斯");  // print 最遠丁滿，最近悟空
console.log("=== Task 2 ===")
let reserves1=[]
let reserves2=[]
let reserves3=[]
function func2(ss, start, end, criteria){ 
let cut1=criteria.split(">=")
let cut2=criteria.split("<=")
let cut3=criteria.split("=")
let result=[]
let answer
let order=[]
let order1=[]
let order2=[]
let order3=[]
for (i=start; i<=end; i++){
    order.push(i)
}
for(i=0; i<order.length; i++){
    if (reserves1.includes(order[i])){
        order1.push(order[i])
    }else if(reserves2.includes(order[i])){
        order2.push(order[i])
    }else if(reserves3.includes(order[i])){
        order3.push(order[i])
    }
}

if(cut1[0]=="c" && Number(cut1[1])<=1200){
    for(i=0; i<services.length; i++){
        if(services[i].c >= Number(cut1[1])){
            result.push(services[i].c)
        }
    }
    let min=Math.min(...result);
    for(i=0; i<services.length; i++){
        if(min==services[i].c){
            answer=services[i].name
            break
        }
    }
}else if(cut1[0]=="r" && Number(cut1[1])<=4.5){
    for(i=0; i<services.length; i++){
        if(services[i].r >= Number(cut1[1])){
            result.push(services[i].r)
        }
    }
    let min=Math.min(...result);
    for(i=0; i<services.length; i++){
        if(min==services[i].r){
            answer=services[i].name
            break
        }
    }
}else if(cut2[0]=="c" && Number(cut2[1])>=800){
    for(i=0; i<services.length; i++){
        if(services[i].c <= Number(cut2[1])){
            result.push(services[i].c)
        }
    }
    let max=Math.max(...result);
    for(i=0; i<services.length; i++){
        if(max==services[i].c){
            answer=services[i].name
            break
        }
    }
}else if(cut2[0]=="r" && Number(cut2[1])>=3){
    for(i=0; i<services.length; i++){
        if(services[i].r <= Number(cut2[1])){
            result.push(services[i].r)
        }
    }
    let max=Math.max(...result);
    for(i=0; i<services.length; i++){
        if(max==services[i].r){
            answer=services[i].name
            break
        }
    }
}else if(cut3[0]=="name"){
    for(i=0; i<services.length; i++){
        if(cut3[1]==services[i].name){
            answer=services[i].name
            break
        }
    }
}else{
    console.log("Sorry")
}

if(answer=="S1" && order1.length == 0){
        reserves1.push(...order)
        console.log(answer)
    }else if(answer=="S2" && order2.length == 0){
        reserves2.push(...order)
        console.log(answer)
    }else if(answer=="S3" && order3.length == 0){
        reserves3.push(...order)
        console.log(answer)
    }else{
        console.log("Sorry")
    }
}
const services=[ 
{"name":"S1", "r":4.5, "c":1000}, 
{"name":"S2", "r":3, "c":1200}, 
{"name":"S3", "r":3.8, "c":800} 
]; 
func2(services, 15, 17, "c>=800");  // S3 
func2(services, 11, 13, "r<=4");  // S3 
func2(services, 10, 12, "name=S3");  // Sorry 
func2(services, 15, 18, "r>=4.5");  // S1 
func2(services, 16, 18, "r>=4");  // Sorry 
func2(services, 13, 17, "name=S1");  // Sorry 
func2(services, 8, 9, "c<=1500");  // S2

console.log("=== Task 3 ===")
function func3(index){ 
let n=25;
let result=[25]
let t=index/4
while (result.length<=index){
    n-=2
    result.push(n);
    n-=3
    result.push(n);
    n+=1
    result.push(n);
    n+=2
    result.push(n);
    t-=1
}
console.log(result[index])
} 

func3(1);  // print 23 
func3(5);  // print 21 
func3(10);  // print 16 
func3(30);  // print 6 

console.log("=== Task 4 ===")
function func4(sp, stat, n){ 
let seat=[]
for(let x=0; x<stat.length; x++){
    if (stat[x]=="1"){
        continue
    }
    seat.push(sp[x])    
}
let best=[]
for(let x=0; x<seat.length; x++){
    if (seat[x]-n>=0){
        best.push(seat[x])
    } 
}
let max=Math.max(...seat);
let min=Math.min(...best);
if (best.length==0){
    for(let x=0; x<sp.length; x++){
    if (sp[x]==max && stat[x]=="0"){
        console.log(x)
    }
}
} else{
    for(let x=0; x<sp.length; x++){
    if (sp[x]==min && stat[x]=="0"){
        console.log(x)
    }
}
}
}
func4([3, 1, 5, 4, 3, 2], "101000", 2);  // print 5 
func4([1, 0, 5, 1, 3], "10100", 4);  // print 4 
func4([4, 6, 5, 8], "1000", 4);  // print 2