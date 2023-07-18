N,M=map(int,input().split())
s=int(input())
li=[]
for i in range(s):
    li.append(list(map(int,input().split())))
axis,l=map(int,input().split())
res=0
for i,j in li:
    if i==axis:
        res+=abs(j-l)
    elif max(i,axis)<=2:
        res+=M+(l+j if (2*N-l-j)>(l+j)else (2*N-j-l))
    elif min(i,axis)>=3:
        j=M-j
        tl=M-l
        res+=N+(tl+j if (2*M-tl-j)>(tl+j)else (2*M-j-tl))
    else:
        if (axis==1 and i==3)or(axis==3 and i==1):
            res+=l+j
        elif (axis==1 and i==4)or(axis==4 and i==1):
            if axis==1:
                res+=N-l+j
            else:
                res+=N-j+l
        elif (axis==2 and i==4)or(axis==4 and i==2):
            res+=2*M-j-l
        elif axis==3 and i==2:
            res+=M-l+j
        elif i==3 and axis==2:
            res+=M-j+l
print(res)
'''
1,2,3,4 북 남 서 동
'''