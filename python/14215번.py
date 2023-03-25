li=sorted(list(map(int,input().split())))
if li[2]<li[1]+li[0]:
    print(sum(li))
else:
    print(2*(li[1]+li[0])-1)