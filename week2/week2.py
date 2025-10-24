print("=== Task 1 ===")
def func1(name):
    place=[ 
    {"id":"悟空", "x":0, "y":0}, 
    {"id":"辛巴", "x":-3, "y":3}, 
    {"id":"貝吉塔", "x":-4, "y":-1},
    {"id":"特南克斯", "x":1, "y":-2}, 
    {"id":"丁滿", "x":-1, "y":4}, 
    {"id":"弗利沙", "x":4, "y":-1}, 
    ]
    left = ["悟空", "辛巴", "貝吉塔", "特南克斯"]
    right = ["丁滿", "弗利沙"]
    me=[]
    distance=[]
    farest=[]
    closest=[]
    for a in place:
        if name==a["id"]:
            me.append(a["x"])
            me.append(a["y"])
    
    if name in left:
        for x in place:
            dx=abs(me[0]-x["x"])
            dy=abs(me[1]-x["y"])
            z=dx+dy
            if x["id"] in right:
                z+=2
            if z>0:
                distance.append(z)
        ma=max(distance)
        mn=min(distance)
        for x in place:
            dx=abs(me[0]-x["x"])
            dy=abs(me[1]-x["y"])
            z=dx+dy
            if x["id"] in right:
                z+=2
            if z==ma:
                farest.append(x["id"])
            if z==mn:
                closest.append(x["id"])
    elif name in right:
        for x in place:
            dx=abs(me[0]-x["x"])
            dy=abs(me[1]-x["y"])
            z=dx+dy
            if x["id"] in left:
                z+=2
            if z>0:
                distance.append(z)
        ma=max(distance)
        mn=min(distance)
        for x in place:
            dx=abs(me[0]-x["x"])
            dy=abs(me[1]-x["y"])
            z=dx+dy
            if x["id"] in left:
                z+=2
            if z==ma:
                farest.append(x["id"])
            if z==mn:
                closest.append(x["id"])
    if len(farest)==0 and len(closest)==0:
        print(f"最遠{farest}，最近{closest}")
    else:
        print(f"最遠{'、'.join(farest)}；最近{'、'.join(closest)}")        
    
func1("辛巴")
func1("悟空")
func1("弗利沙")
func1("特南克斯")

print("=== Task 2 ===")
reserves1=[]
reserves2=[]
reserves3=[]
def func2(ss, start, end, criteria): 
    
    if ">=" in criteria:
        p=criteria.split(">=")
        z=">="
        n=float(p[1])
    elif "<=" in criteria:
        p=criteria.split("<=")
        z="<="
        n=float(p[1])
    elif "=" in criteria:
        p=criteria.split("=")
        z="="
        n=p[1]
    else:
        print("Sorry")
    result=[]
    order=[]
    order={x for x in range(start, end+1)}
    S1=set(reserves1)&order
    S2=set(reserves2)&order
    S3=set(reserves3)&order
    if p[0] == "c" and z==">=" and n<=1200:
        for s in services:
            r=s["c"]-n
            if r>=0:
                result.append(s["c"])
                mi=min(result)        
        for d in services:
            if d["c"]==mi:
                answer=(d["name"])
                break
            
        if answer=="S1" and len(S1)==0:
            reserves1.extend(order)
            print(answer)
        elif answer=="S2" and len(S2)==0:
            reserves2.extend(order)
            print(answer)
        elif answer=="S3" and len(S3)==0:
            reserves3.extend(order)
            print(answer)
        else :
            print("Sorry")

    elif p[0] == "c" and z=="<=" and n>=800:
        for s in services:
            r=s["c"]-n
            if r<=0:
                result.append(s["c"])
                ma=max(result)        
        for d in services:
            if d["c"]==ma:
                answer=(d["name"])
                break  
        if answer=="S1" and len(S1)==0:
            reserves1.extend(order)
            print(answer)
        elif answer=="S2" and len(S2)==0:
            reserves2.extend(order)
            print(answer)
        elif answer=="S3" and len(S3)==0:
            reserves3.extend(order)
            print(answer)
        else :
            print("Sorry")
    elif p[0] == "r" and z==">=" and n<=4.5:
        for s in services:
            r=s["r"]-n
            if r>=0:
                result.append(s["r"])
                mi=min(result)        
        for d in services:
            if d["r"]==mi:
                answer=(d["name"])
                break
            
        if answer=="S1" and len(S1)==0:
            reserves1.extend(order)
            print(answer)
        elif answer=="S2" and len(S2)==0:
            reserves2.extend(order)
            print(answer)
        elif answer=="S3" and len(S3)==0:
            reserves3.extend(order)
            print(answer)
        else :
            print("Sorry")

    elif p[0] == "r" and z=="<=" and n>=3:
        for s in services:
            r=s["r"]-n
            if r<=0:
                result.append(s["r"])
                ma=max(result)        
        for d in services:
            if d["r"]==ma:
                answer=(d["name"])
                break
  
        if answer=="S1" and len(S1)==0:
            reserves1.extend(order)
            print(answer)
        elif answer=="S2" and len(S2)==0:
            reserves2.extend(order)
            print(answer)
        elif answer=="S3" and len(S3)==0:
            reserves3.extend(order)
            print(answer)
        else :
            print("Sorry")
    elif p[0] == "name" :

        if n =="S1" and len(S1)==0:
            reserves1.extend(order)
            print(answer)
        elif n =="S2" and len(S2)==0:
            reserves2.extend(order)
            print(answer)
        elif n =="S3" and len(S3)==0:
            reserves3.extend(order)
            print(answer)
        else :
            print("Sorry")  

    else:
        print("Sorry")

services=[ 
{"name":"S1", "r":4.5, "c":1000}, 
{"name":"S2", "r":3, "c":1200}, 
{"name":"S3", "r":3.8, "c":800} 
] 
func2(services, 15, 17, "c>=800")  # S3 
func2(services, 11, 13, "r<=4")  # S3 
func2(services, 10, 12, "name=S3")  # Sorry 
func2(services, 15, 18, "r>=4.5")  # S1 
func2(services, 16, 18, "r>=4")  # Sorry 
func2(services, 13, 17, "name=S1")  # Sorry 
func2(services, 8, 9, "c<=1500")  # S2 

print("=== Task 3 ===")
def func3(index):
    n=25
    result=[25]
    while len(result)<=index:
        n-=2
        result.append(n)
        n-=3
        result.append(n)
        n+=1
        result.append(n)
        n+=2
        result.append(n)
    print(result[index])

func3(1)  # print 23 
func3(5)  # print 21 
func3(10)  # print 16 
func3(30)  # print 6

print("=== Task 4 ===")
def func4(sp, stat, n): 
    seat=[]
    best=[]
    z=0
    answer=0
    for x in stat :
        if x == "1":
            z+=1
            continue
        seat.append(sp[z])
        z+=1

    for y in seat:
        if y-n>=0:
            best.append(y)

    if len(best) == 0 :
        for y in seat:
            best.append(y)
        ma=max(best)

        for c in sp:
            if c == ma and stat[answer]=="0":
                print(answer)
                break
            answer+=1
    else:
        mi=min(best)
        for c in sp:
            if c == mi and stat[answer]=="0":
                print(answer)
                break
            answer+=1



func4([3, 1, 5, 4, 3, 2], "101000", 2)  # print 5 
func4([1, 0, 5, 1, 3], "10100", 4)  # print 4 
func4([4, 6, 5, 8], "1000", 4)  # print 2 

