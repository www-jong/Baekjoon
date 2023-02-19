c=1
arr=[1 for _ in range(1000001)]
so=[]
dic={}
m=int(1000000**0.5)+1
for i in range(2,m+1):
    if arr[i]==1:
        for j in range(i+i,1000001,i):
            arr[j]=0
for i in range(3,1000001):
    if arr[i]==1:
        so.append(i)
        dic[i]=1

print(so[len(so)-100:])
print(so[:50])
print(len(so))