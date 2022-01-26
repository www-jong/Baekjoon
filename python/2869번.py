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

a,b,c=map(int,input().split());d=0
c-=b
while c>0:c+=b;c-=a;d+=1;
print(d)

a,b,c=map(int,input().split());
d=(c-a)//(a-b)
if (a-b)>c-a:
    print("2")
else:
    print(d+1)

a,b,c=map(int,input().split());
d=(c-a)//(a-b)
if (c-a)<(a-b) and a!=c:
    print("2")
elif a==c:
    print("1")
elif c%(a-b)==0:
    print(d+2)
else:
    print(d+1)


a,b,c=map(int,input().split());
if (c-a)<=(a-b) and a!=c:
    print("2")
elif a==c:
    print("1")
else:
    d=((c-a)//(a-b)+1)
    if c-a<((c-a)//(a-b)+1)*(a-b):
        d+=1
    print(d)

a,b,c=map(int,input().split());d=0
while c>a*(d+1)-b*d:d+=1
print(d+1)

# +
a,b,c=map(int,input().split())
d=(c-b)//(a-b)
if (c-b)%(a-b)!=0:
    d+=1
print(d)

# 이게 정답.. 힘들다
# -


