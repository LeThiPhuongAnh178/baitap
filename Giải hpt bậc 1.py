# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:13:00 2024

@author: Lê Thị Phương Anh
"""

def giai_phuong_trinh_bac_1(a,b):
    if a== 0:
        if b == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -b/a
        print("Nghiệm của phương trình là:", x)
        
        
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
     
giai_phuong_trinh_bac_1(a,b)
