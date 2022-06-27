import re
n=int(input())
ar=[]
de=666

for i in range(0,3000):
    if i==0:srp=""
    else:srp=str(i)
    for y in range(0,4):
        for j in range(-1,1000):
            if j==-1:srf=""
            else:srf=str(j)
            if y==0:srf=srf
            elif y==1:srf="0"+srf
            elif y==2:srf="00"+srf
            elif y==3:srf="000"+srf
            st=int(srp+str(de)+srf)
            if st<=3000000:
                ar+=[st]
ar2=sorted(set(ar))
print(ar2[n-1])
