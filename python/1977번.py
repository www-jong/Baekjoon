M=int(input())
N=int(input())
sum=0
count=10001
if M==N:
    if M**0.5!=int(M**0.5):
        print("-1")
    else:
        print("%d\n%d"%(int(M**0.5),int(M**0.5)))
else:
    for i in range(int(M**0.5)+1 if M**0.5!=int(M**0.5) else int(M**0.5),int(N**0.5)+1):
        sum+=i**2
        if i**2<count:
            count=i**2
    if sum!=0:
        print("%d\n%d"%(sum,count))
    else:
        print("-1")