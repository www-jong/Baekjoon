import math
li=[]
for i in range(int(input())):
    li.append(int(input()))
li.sort()
mins=min(li)
gcds=math.gcd(*li)
ans=[]
if gcds!=1:
    for i in range(1,20):
        if gcds*i<mins:
            ans.append(gcds**i)
else:
    for i in range(2,mins+1):
        tmp=0
        for j in li:
            if tmp==0:
                tmp=j%i
            else:
                if j%i!=tmp:
                    tmp=-1
        if tmp!=-1:
            ans.append(i)
print(*ans)

'''
유클리드 호제법
'''