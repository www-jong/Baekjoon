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
arr=[0 for i in range(0,10500)]
for i in range(1,10000):
    arr[i+sum(list(map(int,str(i))))]=1
    if arr[i]==0:
        print(i)
    
    
# -




