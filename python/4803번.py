g=1
while True:
    res=0
    n,m=map(int,input().split())
    if n==0 and m==0:break
    tree=[[] for i in range(n+1)]
    visit=[0]*(n+1)
    lnode=[i for i in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        tree[a].append(b)
        if lnode[b]==b:
            lnode[b]=a
        else:
            res=''
    print(f'Case {g}: ',end='')
    if res==0:
        print('no trees.')
    elif res==1:
        print('There is one tree.')
    else:
        print(f'A forest of {res} trees.')
    
    g+=1