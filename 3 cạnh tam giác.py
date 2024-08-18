# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:08:58 2024

@author: Lê Thị Phương Anh  
"""
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a > 0 and b > 0 and c > 0 and ( a + b > c) and (a + c > b) and ( b+c > a):
   print (" a,b,c là một cạnh của tam giác")  
else:
    print (" a,b,c không là một cạnh của tam giác")
    
