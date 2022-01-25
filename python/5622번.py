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
a=list(input())
b=[]
for i in a:
    n=ord(i)-65
    if n<3:
        b.append(3)
    elif n<6:
        b.append(4)
    elif n<9:
        b.append(5)
    elif n<12:
        b.append(6)
    elif n<15:
        b.append(7)
    elif n<19:
        b.append(8)
    elif n<22:
        b.append(9)
    elif n<26:
        b.append(10)
print(sum(b))

#숏코딩 
#print(sum(5*min(ord(x),88)//16-17for x in input()))
# A~Z : 65~90
# -





