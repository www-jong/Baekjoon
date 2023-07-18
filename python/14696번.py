N=int(input())

for _ in range(N):
    Ali=[0]*5
    Bli=[0]*5
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    for i in A[1:]:
        Ali[i]+=1
    for i in B[1:]:
        Bli[i]+=1
    for i in range(4,0,-1):
        if Ali[i]!=Bli[i]:
            if Ali[i]>Bli[i]:
                print("A")
            else:
                print("B")
            break
        else:
            if i==1:
                print("D")
                break