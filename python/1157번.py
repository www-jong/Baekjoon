# -*- coding: utf-8 -*-
# +
a=list(input().lower())
arr=[0 for i in range(26)]
check=0
for i in a:
    arr[ord(i)-97]+=1
for j,i in enumerate(arr):
    if i>=max(arr):
        if j!=arr.index(max(arr)):
            check=1
            break
if check==0:
    print(chr(65+arr.index(max(arr))))
else:
    print("?")

        


#from statistics import*
#try:t=mode(input().upper())
#except:t='?'
#print(t)
#파이썬숏코딩 1위인데.. 모듈을썼다

#s=input().upper();m=0
#for i in set(s):
# c=s.count(i)
# if m==c:o='?'
# if m<c:m=c;o=i
#print(o)
# 이건 되게 잘한것같다.
# set은 중복이없는것을 잘이용했다
