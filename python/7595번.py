while True:
    n=int(input())
    if n==0:
        break
    r='*'
    for i in range(1,n+1):
        print(r*i)