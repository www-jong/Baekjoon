N,S=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
res=0
def func(idx,s):
    global res
    if idx==N:
        if sum(s)==S and len(s)!=0:
            res+=1
        return
    func(idx+1,s+[li[idx]])
    func(idx+1,s)
func(0,[])
print(res)