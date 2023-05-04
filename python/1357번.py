x,y=map(int,input().split())
def rev(a):
    tmp=''
    ch=0
    for i in str(a)[::-1]:
        if ch==0 and i==0:
            continue
        tmp+=i
        ch=1
    return int(tmp)
print(rev(rev(x)+rev(y)))