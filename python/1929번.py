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

# +
# 극한의 코드다이어트로 숏코딩랭킹24위! 

m,n=map(int,input().split());l=[1]*(n+1)
for i in range(2,n+1):
 if l[i]==1 and i>=m:print(i)
 l[i::i]=[0]*(n//i)
"""
효율성은 얘가 젤 빠르다.
m,n=map(int,input().split())
arr=[1]*(n+1)
for i in range(2,n+1):
    if arr[i]==1:
        if i>=m:
            print(i)
        arr[i::i]=[0]*(n//i)
"""
"""
m,n=map(int,input().split())
#arr=[1 for i in range(n+1)]
arr=[1]*(n+1)
for i in range(m,n+1):
    ch=0
    if arr[i]==0:
        continue
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                ch=1
                f=i
                arr[f::f]=[0]*(n//f)
                break
        if ch==0 and i!=1:
            print(i)
"""
"""
M, N = map(int,input().split())
l = [1,1]+[0]*N
for i in range(2,N+1):
  if l[i] == 0:
    if i >= M:
      print(i)
    for j in range(i*i,N+1,i):
      l[j] = 1
"""
