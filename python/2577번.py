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

a=1
for i in range(3):
    a*=int(input())
arr=list(map(int,str(a)))
b=[0,0,0,0,0,0,0,0,0,0]
for i in arr:
    b[i]+=1
for i in range(10):
    print(b[i])



