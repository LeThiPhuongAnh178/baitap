# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:21:57 2024

@author: Student
"""
#nhập năm input
nam = int(input("Nhập vào năm sinh : "))

#nhập ngày tháng hiện tại 
from datetime import date
today = date.today()
year = today.year

#tính số ngày đã
live_year = year - nam

#in kết quả
print(f"Năm nay :{live_year} tuổi , sai thì do bạn nhập sai năm sinh!")