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
n=int(input())
arr=[[0 for j in range(n//3+1)]for i in range(n//3+1)]
narr=[]

for i in range(n//3+1):
    for j in range(n//3+1):
        arr[i][j]=n-3*i-5*j
for i in range(n//3+1):
    try:
        narr.append(arr[i].index(0)+i)
    except:
        pass
if len(narr)==0:
    narr.append(-1)
print(min(narr))



# +
# 숏코딩
n=int(input())
print(-(n in[4,7])or n-2*n//5*2)

# 분발하자.. 메모리/시간이며/코드량까지 압도적이네
