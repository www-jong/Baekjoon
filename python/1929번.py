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
m,n=map(int,input().split())
arr=[1 for i in range(n+1)]
for i in range(m,n+1):
    ch=0
    if arr[i]==0:
        continue
    elif arr[i]==1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                ch=1
                f=i
                while f<=n:
                    arr[f]=0
                    f+=f
                break
for i in range(m,n+1):
    if arr[i]==1 and i!=1:
        print(i)
            
    

