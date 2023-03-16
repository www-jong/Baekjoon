for i in range(int(input())):
    C=int(input())
    li=[0]*(4)
    co=[25,10,5,1]
    for i in range(4):
        li[i]+=C//co[i]
        C=C%co[i]
    print(*li)