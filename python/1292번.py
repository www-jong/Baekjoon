n,m=map(int,input().split());a=[0]
for i in range(1,52):exec('a.append(i);'*i)
print(sum(a[n:m+1]))