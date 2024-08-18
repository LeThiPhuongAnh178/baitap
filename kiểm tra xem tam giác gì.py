# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:26:16 2024

@author: Lê Thị Phương Anh  
"""
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a > 0 and b > 0 and c > 0 and ( a + b > c) and (a + c > b) and ( b+c > a):
    if a == b == c:
        print("Tam giác đều.")
    elif a == b or b == c or a == c:
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2 ) or (b**2 + c**2 == a**2 ):
            print("Tam giác vuông cân.")
        else:
            print("Tam giác cân.")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2 ) or (b**2 + c**2 == a**2 ):
        print("Tam giác vuông.")
    else:
        print("Tam giác thường.")
else: 
    print("a,b,c không phải là ba cạnh của một tam giác.")
        
