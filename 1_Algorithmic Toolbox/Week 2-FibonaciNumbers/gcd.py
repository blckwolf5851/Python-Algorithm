# Uses python3
import sys

def gcd_naive(a, b):
    # base case
    if b == 0:
        return a
    r = a % b
    return gcd_naive(b,r)

inp = input()
a, b = map(int, inp.split())
print(gcd_naive(a, b))
