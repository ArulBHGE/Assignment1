# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:36:49 2022

@author: 105042833
"""

import math
odd_count, even_count=0,0
lst_1=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    ele=int(input())
    lst_1.append(ele)
print("the given list is:", lst_1)
for num in lst_1:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even numbers in the list:", even_count)
print("odd numebrs in the list:", odd_count)

'''
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
'''
