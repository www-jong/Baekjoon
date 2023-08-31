n=int(input())
dic={i:0 for i in input().split()}
for i in range(n):
    for j in input().split():
        dic[j]+=1
res=[]
for k,v in dic.items():
    res.append([v,k])
res.sort(key=lambda x:(-x[0],x[1]))
for i,v in res:
    print(v,i)