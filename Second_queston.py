# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:18:23 2024

@author: 和和和
"""

import matplotlib.pyplot as plt
import time


'''
def f_top_down(n):
    if n == 0 or n == 1:
        return n
    else:
        return f_top_down(n-1) + f_top_down(n-2)
'''    
    

def f_top_down(n):
    if n == 4 or n == 5:
        return 1
    elif n <= 3:
        return 0
    
    else:
        return f_top_down(n-1) + f_top_down(n-2)

def f_top_down_list(n):
    
    f_top_down_list_ = []
    for i in range(5, n+1):
        f_top_down_list_.append(f_top_down(i))
        
    return f_top_down_list_

number = 50
a = f_top_down_list(number)
r = list(range(5, number+1))


plt.figure(dpi = 300)
plt.plot(r, a, 'r')   # red line without marker
plt.title('Fibonacci Number F(n), top_down', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('Nunber of F(4)', fontsize = 15)
plt.show()