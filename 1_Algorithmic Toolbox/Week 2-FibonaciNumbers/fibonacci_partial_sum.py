# Uses python3
import sys

def fibonacci_partial_sum_naive(n, m):
    sum = 0
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
        if n < 11:
            sum += v1
        sum += calc
    return sum % 10


n = int(input())
print(fibonacci_partial_sum_naive(n,10))