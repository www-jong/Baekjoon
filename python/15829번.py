N=int(input())
r=0
idx=0
for i in input():
    r+=((ord(i)-96)*(31**(idx)))%1234567891
    idx+=1
print(int(r)%1234567891)