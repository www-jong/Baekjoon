H,W=map(int,input().split())
N=int(input())
li=[]
for i in range(N):
    R,C=map(int,input().split())
    li.append((R,C))

res=0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        for A in [li[i],li[i][::-1]]:
            for B in [li[j],li[j][::-1]]:
                if (A[0]+B[0]<=H and max(A[1],B[1])<=W) or (A[0]+B[0]<=W and max(A[1],B[1])<=H):
                    res=max(res,A[1]*A[0]+B[1]*B[0])
                if (A[1]+B[1]<=H and max(A[0],B[0])<=W) or (A[1]+B[1]<=W and max(A[0],B[0])<=H):
                    res=max(res,A[1]*A[0]+B[1]*B[0])
                if ((A[1]+B[0])<=H and max(A[0],B[1])<=W) or ((A[1]+B[0])<=W and max(A[0],B[1])<=H):
                    res=max(res,A[1]*A[0]+B[1]*B[0])
                if ((A[0]+B[1])<=H and max(A[1],B[0])<=W) or ((A[0]+B[1])<=W and max(A[1],B[0])<=H):
                    res=max(res,A[1]*A[0]+B[1]*B[0])

print(res)
