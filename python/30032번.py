N,D=map(int,input().split())
a={'d':'q','b':'p','q':'d','p':'b'}
b={'d':'b','b':'d','q':'p','p':'q'}
for _ in range(N):
    s=input()
    if D==1:
        print(*[a[i] for i in s],sep="")
    else:
        print(*[b[i] for i in s],sep="")