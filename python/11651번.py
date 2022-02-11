n=int(input())
a=[0 for _ in range(n)]
res=""
for i in range(n):
    w,q=map(int,input().split())
    a[i]=(q+100000)*1000000+w+100000
a.sort()
for i in range(n):
    second=a[i]//1000000 -100000
    first=a[i]%1000000-100000
    res+=str(first)+" "+str(second)+"\n"
print(res)
  