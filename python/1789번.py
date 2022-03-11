a,b=map(int,input().split())
print(*list(map(lambda x:int(x)-a*b,input().split())),sep=" ")