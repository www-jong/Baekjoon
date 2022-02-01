"""
1차시도, 되긴되지만 시간초과
while True:
    n=int(input())
    if n ==0:
        break
    co=0
    for i in range(n+1,n*2+1):
        ch=0
        for j in range(2,i//2+1):
            if i%j==0:
                ch=1
                break
        if ch==0 and i!=1:
            co+=1
    print(co)
"""
n=123456
arr=[1 for i in range(n*2+1)]
for i in range(1,n*2+1):
    ch=0
    if arr[i]==0:
        continue
    elif arr[i]==1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                ch=1
                f=i
                while f<=n*2:
                    arr[f]=0
                    f+=f
                break
while True:
    n=int(input())
    if n==0:
        break
   
    count=0
    for i in range(n+1,n*2+1):
        if arr[i]==1 and i!=1:
            count+=1
    print(count)
            
    
