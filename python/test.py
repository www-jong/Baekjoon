import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline


while True:
    li=list(map(int,input().split()))
    res=0
    if li[0]==0:break
    else:li.pop(0) 
    stk=[]
    for i in li:
        idx=1
        if not stk:
            stk.append(i)
        else:
            if stk[-1]<=i:
                stk.append(i)
            else:
                while stk[-1]>=i:
                    res=max(res,stk.pop()*idx)
                    idx+=1
                    if not stk:
                        break
                res=max(res,i*idx)
                stk.append(i)
    idx=1
    while stk:
        res=max(res,stk.pop()*idx)
        idx+=1
    print(res)

'''
8 1 1 1 1 1 1 1 1
8 1 2 3 4 5 6 7 8
8 1 2 3 4 5 6 7 8
8 1 0 1 0 1 0 1 0
8 0 1 0 1 0 1 0 1
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
5 1000000000 1000000000 1000000000 1000000000 1000000000
5 0 0 0 0 0
7 8 7 1 1 1 9 6
7 9 6 1 1 1 7 6
10 48 59 378 2437 583 1248 214 281 573 43
10 593 532 425 137 647 231 84 698 421 378
10 2 5 9 5 2 1 4 7 4 1
7 0 5 7 5 5 3 1
0
'''