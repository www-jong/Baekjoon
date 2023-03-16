n=1000-int(input())
coin=[500,100,50,10,5,1]
res=0
for i in coin:
    res+=n//i
    n=n%i
print(res)