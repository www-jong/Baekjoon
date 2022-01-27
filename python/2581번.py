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

m=int(input());n=int(input())
count=0
s_sum=0
cc=0
for i in range(m,n+1):
    ch=0
    for j in range(2,i//2+1):
        if i%j==0:
            ch=1
            break
    if ch==0 and i!=1:
        s_sum+=i
        if cc==0:
            count=i
            cc=1
if count==0:
    print("-1")
else:
    print("%d\n%d"%(s_sum,count))


#
