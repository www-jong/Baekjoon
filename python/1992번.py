n=int(input())
maps=["0"*(n+1)]
for i in range(n):
    a="0"+input()
    maps.append(a)
ans=""
def func(st,en):
    global ans
    tmp=0
    half=(en[0]-st[0]+1)//2
    if st==en:
        if maps[en[0]][en[1]]=="1":
            ans+="1"
        else:
            ans+="0"
    else:
        for i in range(st[0],en[0]+1):
            for j in range(st[1],en[1]+1):
                tmp+=int(maps[i][j])
        if tmp==((half*2)**2):
            ans+="1"
        elif tmp==0:
            ans+="0"
        else:
            ans+="("
            func((st[0],st[1]),(en[0]-half,en[1]-half))
            func((st[0],st[1]+half),(en[0]-half,en[1]))
            func((st[0]+half,st[1]),(en[0],en[1]-half))
            func((st[0]+half,st[1]+half),(en[0],en[1]))
            ans+=")"
func((1,1),(n,n))
print(ans)