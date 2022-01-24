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
for i in range(n):
    arr=list(map(int,input().split()))
    del arr[0]
    tot=0
    for j in arr:
        tot+=1 if j>(sum(arr)/len(arr)) else 0
    print("%.3f%%"%(tot/len(arr)*100))




