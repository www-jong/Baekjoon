c=1
arr=[1 for _ in range(1000001)]

m=int(1000000**0.5)
for i in range(2,m+1):
    if arr[i]==1:
        for j in range(i+i,1000001,i):
            arr[j]=0

while c!=0:
    c=int(input())
    b=0
    for i in range(2,c-1):
        if arr[i]==1 and arr[c-i]==1:
            print("%d = %d + %d"%(c,i,c-i))
            b=1
            break        
    if b==0 and c!=0:
        print("Goldbach's conjecture is wrong.")
        