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
for i in range(n):
    a=str(input())
    point=0
    arr=[]
    for j in a:
        if len(arr)==0:
            if j=='O':
                arr.append(1)
            else:arr.append(0)
        elif j=='O':
            arr.append(arr[-1]+1)
        else:arr.append(0)
    print(sum(arr))
            
            
# -


