N=int(input())
li=list(map(int,input().split()))+[10**9]
res=0
tmp=[0]
for i in range(len(li)):
    if tmp[-1]-1!=li[i] and li[i]!=tmp[-1]+1:
        res+=min(tmp)
        print(min(tmp),li[i])
        tmp=[li[i]]
    else:
        tmp.append(li[i])
print(res)