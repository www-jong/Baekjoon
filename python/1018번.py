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
m,n=map(int,input().split())
w='WB'
b='BW'
ww=w*25
bb=b*25
www=[]
bbb=[]
for i in range(1,26):
    if i%2==0:
        www+=[ww]
        bbb+=[bb]
    else:
        www+=[bb]
        bbb+=[ww]
ans=[]
for i in range(m):
    ans+=[input()]
an=[]
res1=[]

rs1=0
rs2=0
for ii in range(0,len(ans)-7):
    for jj in range(0,len(ans[0])-7):
        rs1=0
        rs2=0
        for i in range(8):
            for j in range(8):
                if ans[i+ii][j+jj]!=www[i][j]:
                    rs1+=1
                if ans[i+ii][j+jj]!=bbb[i][j]:
                    rs2+=1
        res1+=[min(rs1,rs2)]
print(min(res1))
