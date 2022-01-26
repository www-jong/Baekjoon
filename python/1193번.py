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

n=int(input());a=0;i=0
while n>0:a+=1;n-=a;i+=1; 
if i%2==0:
    print("%d/%d"%((i+n),(1-n)))
else:
    print("%d/%d"%((1-n),(i+n)))





