a=[0,31,28,31,30,31,30,31,31,30,31,30,31]
b=['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
n,m=map(int,input().split())
for i in range(1,n):
    m+=a[i]
print(b[m%7])
