d=1
while True:
    li=list(map(int,input().split()))
    if len(li)==1 and li[0]==0:
        break
    li=li[1:]
    if len(li)%2==0:
        print('Case %d: %.1f'%(d,(li[len(li)//2-1]+li[len(li)//2])/2))
    else:
        print('Case %d: %.1f'%(d,li[len(li)//2]))
    d+=1