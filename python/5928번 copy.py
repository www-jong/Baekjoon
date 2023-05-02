d,h,m=map(int,input().split())
res=(d-11)*60*24+(h-11)*60+(m)-11
print(res if res>=0 else -1)