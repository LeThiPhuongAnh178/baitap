# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:56:21 2024

@author: Student
"""
#nhập số km đã đi
km = float(input("số km mà bạn đã đi là: "))
if km <= 1 :
    m = km*20
elif 1 <= km <= 3:
    m = km*13
elif 4 <= km <= 8:
    m = km*12
else:
    m = km*10
if m > 100: 
    m = m - (m*0.08)
print(f"số tiền phải trả là {m}k ")
    