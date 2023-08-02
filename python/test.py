li=range(1,13)
for m in range(int(input())):
    N,K=map(int,input().split())
    res=0
    r=[1 if len([j for j in li if (1<<j)&i])==N and sum([j for j in li if (1<<j)&i])==K else 'pass' for i in range(2**12)]
    print(r)
