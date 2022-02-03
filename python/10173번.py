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

while True:
    arr=input()
    arrr=arr.lower()
    if arrr.find('nemo') != -1:
        print("Found")
    elif "eoi" in arrr and "EOI" in arr:
        break
    else:
        print("Missing")
