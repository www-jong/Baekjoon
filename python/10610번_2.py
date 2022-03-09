n=input();arr=list(n)
if "0" not in arr:print("-1")
else:
    arr=sorted([int(i) for i in arr],reverse=True)
    if sum(arr)%3==0:print(*arr,sep="")
    else:print("-1")