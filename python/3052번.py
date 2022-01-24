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

a=list(0 for i in range(0,42))
ans=0
for i in range(10):
    a[int(input())%42]+=1
for i in a:
    if i>0:
        ans+=1
print(ans)


