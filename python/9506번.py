while True:
    s=int(input())
    li=[]
    if s==-1:break
    for i in range(1,s+1):
        if s%i==0:li.append(i)
    if sum(li)==s:
        