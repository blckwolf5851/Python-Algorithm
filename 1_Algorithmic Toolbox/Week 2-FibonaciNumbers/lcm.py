# Uses python3
import sys
import math

def lcm_naive(a, b):
    # base case
    if b == 0:
        return a
    r = a % b
    return lcm_naive(b,r)
inp = input()
a, b = map(int, inp.split())
s = int(b/lcm_naive(a,b))
print(int(s*a))