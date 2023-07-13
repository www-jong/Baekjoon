N=int(input())
li=list(map(int,input().split()))
li.sort()
x=int(input())
st=0
end=N-1
res=0
while st<end:
    if st>=N or end<0:
        break
    tmp=li[st]+li[end]
    if tmp==x:
        res+=1
        st+=1
        end-=1
    elif tmp>x:
        end-=1
    else:
        st+=1

print(res)

'''
7
5 6 7 8 9 50 51 52
101
9

'''