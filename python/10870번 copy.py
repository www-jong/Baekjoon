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
p=[0,1]
if n>=2:
    for i in range(2,n+1):
        p.append(p[i-1]+p[i-2])
    print(p[n])
else:
    print(n)


# -


# 숏코딩
a=0;b=1
exec("a,b=b,a+b;"*int(input()))
print(a)
# 이런방법이!
