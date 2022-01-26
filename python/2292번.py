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
a=2
for i in range(100000):
    if n==1:
        print(n)
        break
    elif n>=a and n<=a+i*6-1:
        print(i+1)
        break
    a+=i*6
    
#다른방법
#a=int(input());i=0
#while a>1:i+=1;a-=6*i;
#print(i+1)

# -

a=int(input());i=0
while a>1:i+=1;a-=6*i;
print(i+1)




