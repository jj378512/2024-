# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:05:29 2024

@author: 和和和
"""

#Fibonacci Number F(n) = F(n-1) + F(n-2)-----top_down(divide and conqure/ pure recursive)

import matplotlib.pyplot as plt
import time

#設定F(n)的n
number = int(input('輸入F(n)之n：'))

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

def f_bottom_up_list(n):
    
    f_top_down_list_ = []
    for i in range(5, n+1):
        f_top_down_list_.append(f_top_down(i))
        
    return f_top_down_list_


start_time = time.time()
a = f_bottom_up_list(number)
end_time = time.time()

#計算程式執行時間
execution_time = end_time - start_time
print("程式執行時間：", execution_time, "秒")

r = list(range(5, number+1))


plt.figure(dpi = 300)
plt.plot(r, a, 'r')   # red line without marker
plt.title('Fibonacci Number F(n), top_down', fontsize = 15) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('Nunber of F(4)', fontsize = 15)
plt.show()