x=int(input())
n=64
c=0
while x!=0:
     for i in range(0,7):
        if x>=64/(2**i):
            x-=64/(2**i)
            c+=1
            break
print(c)