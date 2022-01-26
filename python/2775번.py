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

arr=[[i for i in range(15)] for i in range(15)]
for i in range(1,15):
    for j in range(1,15):
        arr[j][i]=arr[j][i-1]+arr[j-1][i]
for i in range(int(input())):
    a=int(input())
    b=int(input())
    print(arr[a][b])



