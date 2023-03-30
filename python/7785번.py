N=int(input())
dic={}
for i in range(N):
    name,log=map(str,input().split())
    if log=='enter':
        dic[name]=1
    else:
        del dic[name]
li=[]
for i in dic.keys():
    li.append(i)
li.sort(reverse=True)
print(*li,sep="\n")