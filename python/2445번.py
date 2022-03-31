a=" ";b="*"
for i in range(1,(n:=int(input()))+1):
    print(b*i+a*(n*2-2*i)+b*i)
for i in range(n-1,0,-1):
    print(b*i+a*(n*2-2*i)+b*i)