# -*- coding: utf-8 -*-
"""add&sub.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k3sAu_LN3kBI5U9q6SyJrrGZGJfGytKn
"""

a=float(input("please enter the first number A:"))
b=float(input("please enter the second number B:"))
t=int(input("type 1 if you want'+'\n type 2 if you want'-'\n taye 3 if you want'*'\n type 4 if you want'/'"))
if(t==1):
   a=float(a+b)
   print(a)
elif(t==2):
   a=float(a-b)
   print(a)
elif(t==3):
   a=float(a*b)
   print(a)
elif(t==4 and b!=0):
   a=float(a/b)
   print(a)
elif(t==4 and b==0):
  print("divided in zero")
else:
  print("please type in 1,2,3,4")