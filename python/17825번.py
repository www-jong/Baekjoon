absol={10:13,20:21,30:31}
graph=[0]*42
point=[0]*42
res=0
for i in range(0,39,2):
    graph[i]=i+2
    point[i]=i
graph[13]=15
point[13]=13
graph[15]=19
point[15]=16
graph[19]=25
point[19]=19
graph[21]=23
point[21]=22
graph[23]=25
point[23]=24
graph[31]=33
point[31]=28
graph[33]=35
point[33]=27
graph[35]=25
point[35]=26
graph[25]=37
point[25]=25
graph[37]=39
point[37]=30
graph[39]=40
point[39]=35
graph[40]=41
graph[41]=41
point[41]=0
point[40]=40
li=list(map(int,input().split()))
def func(horse,cnt,idx,move):
    global res
    if idx==len(li):
        res=max(res,cnt)
        return
    for i in range(4):
        if horse[i]==41:
            continue
        tmp_horse=horse[i]
        now_horse=horse[i]
        for j in range(li[idx]):
            if now_horse in absol and j==0:
                now_horse=absol[now_horse]
            else:
                now_horse=graph[now_horse]
        if now_horse!=41 and now_horse in horse:
            continue
        horse[i]=now_horse
        func(horse,cnt+point[now_horse],idx+1,move+[i])
        horse[i]=tmp_horse
func([0,0,0,0],0,0,[])
print(res)
