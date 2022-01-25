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
st=list(input())
ans=[-1 for i in range(26)]
for i,j in enumerate(st):
    if ans[ord(j)-97]==-1:
        ans[ord(j)-97]=i
print(*ans)

# print(*map(input().find,map(chr,range(97,123))))
# find? 뭐지
# str.find(찾을문자) 
# or str.find(리스트)
# 즉,a~z에서 입력된 str의 인덱스를 반환하고, 없다면 -1
# 완전 find를 위한 문제였다.

