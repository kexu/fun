# -----------------------------------------------------------------------------
# File          : calc_pi.py
# Description   : calculate the value of PI by Monte Carlo simulation 
# Author        : Ke Xu, kkexu@outlook.com
# History        
# 1.0 2017/10/22: initial version
# -----------------------------------------------------------------------------

from random import random
def pi(n):
    t = 0
    for kk in range(n):
        x = random() ** 2
        y = random() ** 2
        if x + y <= 1:
            t += 1
    print n
    print t
    return 4.0000*t/n

print (pi(10**7))


