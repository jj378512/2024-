# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:18:38 2024

@author: 和和和
"""

import matplotlib.pyplot as plt

#Fibonacci Number F(n) = F(n-1) + F(n-2)-----bottom_up(dynamic-programming-like)


#設定F(n)的n
number = int(input('輸入F(n)之n：'))

#計算F(n) = F(n-1) + F(n-2) 之 F(n)
def f_bottom_up(n):
    f1 = 0
    f2 = 1
    f3 = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        
        return f3

'''
f_bottom_up_list_ = []
for i in range(0, 10+1):
    #print(f_bottom_up(i)) 
    f_bottom_up_list_.append(f_bottom_up(i))

a = f_bottom_up_list_

'''

#將F(n)做成list
def f_bottom_up_list(n):
    
    f_bottom_up_list_ = []
    for i in range(0, n+1):
        f_bottom_up_list_.append(f_bottom_up(i))
        
    return f_bottom_up_list_


a = f_bottom_up_list(number)
r = list(range(0, number+1))


plt.figure(dpi = 300)
plt.plot(r, a, 'r')   # red line without marker
plt.title('Fibonacci Number F(n), bottom_up', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('F(n)', fontsize = 15)
plt.show()








