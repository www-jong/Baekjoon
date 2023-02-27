S1,S2,S3=map(int,input().split())
dic={}
for i in range(1,S1+1):
    for j in range(1,S2+1):
        for k in range(1,S3+1):
            if i+j+k not in dic:
                dic[i+j+k]=1
            else:
                dic[i+j+k]+=1
res=[0,0]
for k,v in dic.items():
    if v>res[0]:
        res=v,k
print(res[1])
print(res[0])