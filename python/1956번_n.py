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
V,E=map(int,input().split())

for i in range(E):
    arr=[[100000000 for i in range(V+1)] for j in range(V+1)]
    a,b,c=map(int,input().split())
    if arr[a][b]!=0:  # 이미 길이 있다면 최소값으로
        arr[a][b]=min(c,arr[a][b])
    else: #길이없다면 그냥 넣기
    arr[a][b]=c

for i in range()
print(arr)
# -





