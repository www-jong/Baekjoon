N=input()
li=list(map(int,input().split()))
dic={}
for i in li:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
r=0
for i in li:
    for j in dic:
        if i-j in dic:
            if not((j==(i-j) and dic[j]<=2) or(i==j and dic[i]==1)or(i==(i-j)and dic[i]==1)):
                r+=1
                print(i,j,i-j)
                break
print(r)