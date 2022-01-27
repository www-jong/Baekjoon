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

input();n=map(int,input().split());count=0;
for i in n:
    ch=0
    for j in range(2,i//2+1):
        if i%j==0:
            ch=1
            break
    if ch==0 and i!=1:
        count+=1
print(count)

