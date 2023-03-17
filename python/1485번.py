T=int(input())
for i in range(T):
    li=[]
    for i in range(4):
        li.append(list(map(int,input().split())))
    len=[]
    for i in range(4):
        for j in range(i+1,4):
            x1,y1=li[i]
            x2,y2=li[j]
            len.append((x2-x1)**2+(y2-y1)**2)
    len.sort()
    if len[0]==len[1]==len[2]==len[3] and len[4]==len[5]:
        print(1)
    else:
        print(0)