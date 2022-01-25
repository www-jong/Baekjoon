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
a,b=map(int,input().split())
a=list(reversed(list(str(a))))
b=list(reversed(list(str(b))))
a=int(''.join(a))
b=int(''.join(b))
print(max(a,b))

#숏코딩예제들
#print(max(input()[::-1].split()))
#이런...방법이
#a b 입력했을때, a를 뒤집고, b를 뒤집고 분리해서..?
#abc def 를 fed cba 로 뒤집고, 분리해서 크기비교..
