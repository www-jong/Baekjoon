a=" ";b="*"
n=int(input())
for i in range(n,0,-1):
    print(a*(n-i)+b*(2*i-1))