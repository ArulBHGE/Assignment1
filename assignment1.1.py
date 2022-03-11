# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:06:55 2022

@author: 105042833
"""

n=int(input("enter the number upto which fibonacci number is required:"))
n1,n2=1,1
count=0
if n<= 0:
    print("please enter a positive integer")
elif n==1:
    print("fibonacci sequence upto",n,"is:")
    print(n1)
else:
    print("Fibonacci sequence upto",n, "is:")
    while n1<=n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
        pass