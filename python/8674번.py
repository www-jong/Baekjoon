a,b=map(int,input().split())
print(min((a-(a//2)*2)*b,(b-(b//2)*2)*a))