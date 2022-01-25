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
for i in range(int(input())):
    a,b=input().split()
    c=""
    for j in list(b):
        c+=j*int(a)
    print(c)
    
#  for r,_,*s,_ in[*open(0)][1:]:print(''.join(c*int(r)for c in s))
# 넘어가자..

# -


