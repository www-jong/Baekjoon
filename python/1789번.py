s=int(input())
n=0
count=0
if s==1:
    print(1)
else:
    for i in range(1,s+1):
        if s>=n+i:
            n+=i
            count+=1
        elif s<n+i:
            print(count)
            break