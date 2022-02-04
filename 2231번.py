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

n=int(input())
s=5
ans=0
if n<=9:
    print("0")
else:        
    while n!=ans:
        ans=s+sum([int(i) for i in str(s)])
        s+=1
        if n<=s:
            print("0")
            break
        elif n==ans:
            print(s-1)
            break
#잘되는거같은데 자꾸 틀렸댄다 ㅠ
# 해결.

n=int(input())
n_arr=list(map(int,str(n)))
if n<18:
    m=n-9*(len(n_arr)-1)
elif n<1000:
    m=n-9*(len(n_arr))
else:
    m=n-1000
ch=0
if n<=9:
    if n%2==0:
        print(int(n/2))
        ch=1
    else:
        ch=0
else:
    for i in range(m,n+1):
        m_s=i+sum([int(j) for j in str(i)])
        if n==m_s:
            print(i)
            ch=1
            break
if ch==0:
    print("0")
    


