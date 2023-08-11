import random
from time import time
st_time=time()
n=1000
rs=open('./testcase.txt','w')
rs.write(str(n)+"\n")
for i in range(n):
    rs.write(str(int(random.random()*9999))+" "+str(int(random.random()*9999))+"\n")
for i in range(100000000):
    pass
rs.close()
print(time()-st_time)