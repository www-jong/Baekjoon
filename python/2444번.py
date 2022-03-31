a=" ";b="*"
for i in range(1,(n:=int(input()))+1):
    print(a*(n-i)+b*(2*i-1))
for i in range(n-1,0,-1):
    print(a*(n-i)+b*(2*i-1))