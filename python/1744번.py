N=int(input())
li=[]
res=0
for i in range(N):
    n=int(input())
    if n!=0:
        li.append(n)
li.sort(reverse=True)

print(li)
tmp=li[0]

for i in range(1,len(li)):
    if tmp!=-1001:
        if tmp<0:
            if li[i]<0:
                res+=tmp*li[i]
                tmp=-1001
            elif li[i]>0:
                res+=tmp
                tmp=li[i]
        elif tmp>0:
            if tmp!=1:
                res+=tmp*li[i]
                tmp=-1001
            else:
                res+=tmp
                tmp=-li[i]
    else:
        if li[i]==1:
            res+=1
        else:
            tmp=li[i]
if tmp!=-1001:
    res+=tmp
print(res)