import sys
input=sys.stdin.readline
while True:
    tmp=list(map(int,input().split()))
    res=tmp[0]
    if tmp[0]==0:
        break
    li=[]
    for i in range(1,tmp[0]):
        li.append([tmp[i],i])
    sort_li=sorted(li,key=lambda x:(x[0],x[1]))
    before_data=[0,[]]
    for val,idx in sort_li:
        ttmp=[]
        ttmp.append(idx)
        
'''
1, 3, 4, 7 ...

1 -> 0, 3 ,5, 6 idx
3 -> [i-1][0]+1


'''