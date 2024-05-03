# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:15:15 2024

@author: 和和和
"""

import matplotlib.pyplot as plt
import time

#設定F(n)的n
number = 100


def f_top_down(n):
    if n == 0 or n == 1:
        return n
    else:
        return f_top_down(n-1) + f_top_down(n-2)
  


def f_top_down_list(n):
    
    f_top_down_list_time = []
    for i in range(0, n+1):
        start_time = time.time()
        Kernel = f_top_down(i)
        end_time = time.time()
        
        #計算程式執行時間
        execution_time = end_time - start_time
        
        f_top_down_list_time.append(execution_time)
        
        print("程式執行時間：", execution_time, "秒")
        
    return f_top_down_list_time



a = f_top_down_list(number)
r = list(range(0, number+1))


plt.figure(dpi = 300)
plt.plot(r, a, 'r')   # red line without marker
plt.title('Fibonacci Number F(n), top_down', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('F(n)', fontsize = 15)
plt.show()