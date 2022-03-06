min=100
sum=0
for i in range(7):
    n=int(input())
    if n%2!=0:
        sum+=n
        if min>n:
            min=n
if sum!=0:
    print(sum)
    print(min)
else:
    print("-1")
