import sys
input=sys.stdin.readline
li=[]
while True:
    a=int(input())
    if not a:
        break
    li.append(a)
li.sort(reverse=True)

res=[]
for i in range(len(li)):
    c=0
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
            if li[i]<li[j]+li[k] and sum(res)<sum([li[i],li[j],li[k]]):
                res=[li[i],li[j],li[k]]
                c=1
                break
            if c:
                break
    if c:
        break
print(*res)
if not res:
    print('NIE')