a,b,c=map(int,input().split())
if a==b and b==c:
    print(10000+1000*a)
elif a==b or b==c or a==c:
    print(1000+100*(a if a==b else (b if b==c else a)))
else:
    print(100*max(a,b,c))