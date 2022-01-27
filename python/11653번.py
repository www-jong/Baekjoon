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

n=int(input())
a=2
while True:
    if n%a==0:
        print(a)
        n=n/a
    elif n==1:
        break
    else:
        a+=1


# # 
