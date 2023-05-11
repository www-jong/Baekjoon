#li=list(map(int,input().split()))
li=[4,10,8,2,9,3,1,6,7,5]
#li=[8,18,15,16,9,10,5,7,4,1,6,11,2,3,12,14,19,13,20,17]
k=4
co=0

def check(a,b):
    tmpli=[]
    for i in range(a,b+1):
        tmpli.append(li[i])
    c=1    
    while True:
        if c not in tmpli:
            return c
        c+=1
    
for i in range(len(li)):
    for j in range(i,len(li)):
        if check(i,j)!=k:
            co+=1
        else:
            print(f'{i+1}:{j+1}')
print(f'co:{co} , len:{len(li)}')

'''
s=list(map(int,input().split()))
count=0
while sum(s)!=0:
    if s[0]>0:
        s[0]-=1
    for i in range(1,len(s)):
        if s[i]>0:
            s[i]-=1
            s[i-1]+=1
    count+=1
    print(s)
print(count)
print(len(s))
'''