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

n=input()
n=n.replace("apa","ㅁ").replace("epe","ㄷ").replace("ipi","ㅑ").replace("opo","ㅐ").replace("upu","ㅕ")
n=n.replace("ㅁ","a").replace("ㄷ","e").replace("ㅑ","i").replace("ㅐ","o").replace("ㅕ","u")
print(n)
