res=0
co=0
dic={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
for i in range(20):
    _,n,g=map(str,input().split())
    if g=='P':
        continue
    else:
        res+=float(n)//1*dic[g]
        co+=float(n)//1
print(res/max(co,1))