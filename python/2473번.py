N=int(input())
li=list(map(int,input().split()))
li.sort()
res=[10**11,0,0,0]
for a in range(len(li)-2):
    b,c=a+1,len(li)-1
    while b<c:
        now=li[a]+li[b]+li[c]
        if abs(now)<=abs(res[0]):
            res=[abs(now),li[a],li[b],li[c]]
        if now<0:
            b+=1
        elif now>0:
            c-=1
        else:
            break
print(*sorted(res[1:]))