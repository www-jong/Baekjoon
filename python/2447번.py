# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# numpy 사용
import numpy as np
n=int(input())
arr=[["*","*","*"],["*"," ","*"],["*","*","*"]]
narr=[[" "," "," "],[" "," "," "],[" "," "," "]]
ans=[]
for i in range(1,int((n**(1/3)))):
    ar1=np.concatenate((arr,arr,arr),axis=1)
    ar2=np.concatenate((arr,narr,arr),axis=1)
    ar3=ar1
    arr=np.concatenate((ar1,ar2,ar3),axis=0)
    
    na1=np.concatenate((narr,narr,narr),axis=1)
    narr=np.concatenate((na1,na1,na1),axis=0)
for i in range(0,n):
    print(*arr[i][:],sep="")


# +
n=int(input())
arr=[["*","*","*"],["*"," ","*"],["*","*","*"]]
narr=[[" "," "," "],[" "," "," "],[" "," "," "]]
for i in range(1,int((n**(1/3)))):
    ar1=list(map(list.__add__,list(map(list.__add__,arr,arr)),arr))
    ar2=list(map(list.__add__,list(map(list.__add__,arr,narr)),arr))
    arr=ar1+ar2+ar1
    
    na1=list(map(list.__add__,list(map(list.__add__,narr,narr)),narr))
    narr=na1*3
for i in range(0,n):
    print(*arr[i][:],sep="")
    
## 이것도 되긴되는데.. 메모리초과

# +
#배열합치기를 사용하면 메모리소비가 크다.
#다르게 해보자
#어차피 배열은 써야하므로
# 행을 문자열합치기로 바꿔보기
n=int(input())
arr=[["0"]*n for i in range(n)]
arr[0]="***"
arr[1]="* *"
arr[2]="***"
emp=" "
# 애초에 세제곱근 구하는게 틀렸었다
# 새로 값을 만들어야함.
check_n=n
co=0
while True:
    check_n/=3
    co+=1
    if check_n==1:
        break
#for i in range(1,int((n**(1/3)))):
for i in range(1,co):
    emp=emp*3
    for j in range(3**i,(3**i)*2):
        arr[j]=arr[j-3**i]+emp+arr[j-3**i]
    for j in range(0,3**i):
        arr[j]=arr[j]*3
    for j in range((3**i)*2,(3**i)*3):        
        arr[j]=arr[j-(3**i)*2]
if n==3:
    for i in range(3):
        print(arr[i])
else:
    for i in range(n):
        print(arr[i])

    
