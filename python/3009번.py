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

a=[[0 for j in range(1001)] for i in range(2)]
for i in range(3):
    x,y=map(int,input().split())
    a[0][x]+=1;a[1][y]+=1;
print("%d %d"%(a[0].index(1),a[1].index(1)))

