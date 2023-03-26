res=2
for i in range(1,int(input())+1):
    res+=res-1
print(res**2)