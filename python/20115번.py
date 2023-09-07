N=int(input())
li=sorted(list(map(int,input().split())))
res=li.pop()
for i in li:
    res+=i/2
print(res)