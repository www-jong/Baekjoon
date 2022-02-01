l=list(map(int,input().split()))
l[2]-=l[0]
l[3]-=l[1]
print(min(l))