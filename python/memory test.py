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
import psutil
dic={}
for i in range(300000,-1,-1):
    dic[i]=i*2

p=psutil.Process()
print("%10.5f"%(p.memory_info().rss/2**20))
b=dict(reversed(dic.items()))

## 이것도 되긴되는데.. 메모리초과
# -

# n=int(input())
# def star(n):
#     if n==3:
#         return [['*','*','*'],['*',' ','*'],['*','*','*']]
#     x=[[0]*n for i in range(n)]
#     a=star(n//3)
#     for i in range(n):
#         for j in range(n):
#             if i//(n//3)==j//(n//3)==1:
#                 x[i][j]=' '
#             else:
#                 x[i][j]=a[i%(n//3)][j%(n//3)]
#     return x
# a=star(n)
# for i in range(n):
#     for j in range(n):
#         print(a[i][j],end='')
#     print(end='\n')
