#Uses python3

import sys
from math import *
def swap(a,i,n):
    temp = a[i]
    a[i] = a[n]
    a[n] = temp
def largest_number(a):
    #write your code here
    res = ''
    
    a.sort(reverse = True)
    for i in range(len(a)):
        for i in range(len(a)-1):
            if a[i+1][-len(a[i+1])+1] > a[i][-len(a[i])+1] and a[i][0] == a[i+1][0]:
                swap(a,i,i+1)
    for i in a:
        res += i

    return res
n = input()
inp = input()
a = inp.split()
print(largest_number(a))
    
