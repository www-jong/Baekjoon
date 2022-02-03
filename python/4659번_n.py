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

while n:=input()!="end":
        

import re
arrr=input()
a=len(re.findall('a|e|i|o|u',arrr))
b=len(re.findall('([^a|e|i|o|u]){3}|([a|e|i|o|u]{3})',arrr))
c=len(re.findall('([a-df-np-z])'))


