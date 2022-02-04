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
n,m=map(int,input().split())
ar=list(map(int,input().split()))
ar.sort()
n=len(ar)
arr=[]
while ar[n-1]<m:
    if ar[n-1]>=m:
        del ar[n-1]
    else: 
        n==0
        break
    n-=1
for a in range(len(ar)-2):
    for b in range(a+1,len(ar)-1):
        if ar[a]+ar[b]>m:
            break
        for c in range(b+1,len(ar)):
            s=ar[a]+ar[b]+ar[c]
            if s>m:
                break
            elif s<=m:
                arr.append(s)
print(max(arr))

                
    
# -

#숏코딩
[N,M],c=eval('map(int,input().split()),'*2)
from itertools import*;print(max(i for i in map(sum,combinations(c,3))if i<=M))


