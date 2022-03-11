# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:36:49 2022

@author: 105042833
"""

import math
odd_count, even_count=0,0
list_x=input("enter the list for counting odd and even:")
y=list(list_x)
z=list(map(int, list_x))
print(z)
print(type(z))
for num in z:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even numbers in the list:", even_count)
print("odd numebrs in the list:", odd_count)

