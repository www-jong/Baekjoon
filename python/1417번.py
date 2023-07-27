N=int(input())
li=[int(input()) for _ in range(N)]
if N==1:
    print(0)
else:
    check=li.pop(0)
    li.sort(reverse=True)
    res=0
    while True:
        if check>li[0]:
            break
        li[0]-=1
        check+=1
        res+=1
        if len(li)>=2 and li[0]<li[1]:
            li.sort(reverse=True)

    print(res)
