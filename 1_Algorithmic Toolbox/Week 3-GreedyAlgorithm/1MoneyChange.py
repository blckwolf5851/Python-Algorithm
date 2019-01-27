# Uses python3
import sys

def get_change(m):
    #write your code here
    n = 0
    money = [10,5,1]
    for i in money:
        while i <= m:
            m -= i
            n += 1
    return n

m = int(input())
print(get_change(m))
