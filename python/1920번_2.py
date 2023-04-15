N=int(input())
N_li=list(map(int,input().split()))
dic={int:0 for int in N_li}
M=int(input())
M_li=list(map(int,input().split()))
for i in M_li:
    if i in dic:
        print(1)
    else:
        print(0)