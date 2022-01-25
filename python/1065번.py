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

count=0
for i in range(1,1+int(input())):
    if i<100:
        count+=1
    else:
        arr=list(map(int,str(i)))
        check=1
        for j in range(len(arr)-2):
            if (arr[j+1]-arr[j])!=(arr[j+2]-arr[j+1]):
                check=0
                break
        if check==1:count+=1
print(count)
        




