import math
li=[]
for i in range(int(input())):
    li.append(int(input()))
li.sort(reverse=True)
li2=[li[0]-li[1]]
for i in range(1,len(li)-1):
    li2.append(li[i]-li[i+1])
mins=min(li)
gcds=math.gcd(*li2)
ans=[gcds]
for i in range(2,gcds//2+1):
    if gcds%i==0:
        ans.append(gcds//i)
ans.sort()
print(gcds)
print(*ans)

'''
유클리드 호제법
'''