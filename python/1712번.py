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
a,b,c=map(int,input().split())
if b>=c:print("-1")
else:print(int(a/(c-b))+1)
    
#숏코딩
# a,b,c=map(int,input().split());print(-(c<=b)or a//(c-b)+1)
# 이게되네;
# -


