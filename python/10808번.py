b=[0]*26
a=list(map(lambda x:ord(x)-97,list(input())))
for i in a:
    b[i]+=1
print(*b,sep=" ")