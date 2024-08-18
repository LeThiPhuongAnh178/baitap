# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:38:46 2024

@author: Lê Thị Phương Anh  
"""

distance = float(input("Nhập điểm trung bình GPA: "))

if distance < 3.5:
    print("Học lực Kém")
elif distance >= 3.5 and distance <= 5.0:
    print("Học lực Yếu")
elif distance >= 5.0 and distance <= 7.0:
    print("Học lực Trung Bình")
elif distance >= 7.0 and distance <= 8.0:
    print("Học Lực Khá")
elif distance >= 8.0 and distance <= 9.0:
    print("Học lực Giỏi")
elif distance >= 9.0 and distance <= 10:
    print("Học lực Xuất Sắc")
    
    