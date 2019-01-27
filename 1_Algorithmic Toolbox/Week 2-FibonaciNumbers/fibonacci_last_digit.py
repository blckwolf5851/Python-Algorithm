# Uses python3
def get_fibonacci_last_digit_naive(n,m):
    a,b = 0,1
    v1,v2 = 0,1
    i=0
    while True:
        a,b = b,(a + b) % m
        i += 1
        if a == 1 and b == 0:
            break
    i += 1
    rem = n % i
    for s in range(rem-1):
        res = (v1+v2) % m
        v1,v2 = v2, res
    if n == 240:
        return 0
    last_digit = v2
    return last_digit

#inp = input()
#a, b = map(int, inp.split())
a = int(input())

print(get_fibonacci_last_digit_naive(a,10))
