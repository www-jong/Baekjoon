n=int(input())
e={}
arr=[[0,0] for i in range(n)]
for i in range(n):
    a,b=map(str,input().split())
    e[i]={b:int(a)}
    arr[i][0]=int(a)
    arr[i][1]=i
arr.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    ars=""
    for j in e[arr[i][1]].keys():
        name=j
        age=int(e[arr[i][1]].get(j))
    ars+=str(age)+" "+name
    print(ars)
