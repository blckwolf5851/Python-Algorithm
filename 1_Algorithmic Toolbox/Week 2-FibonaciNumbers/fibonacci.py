# Uses python3
def calc_fib(n):
    fib=[0,1]
    if n == 0:
        return 0
    if n==1:
        return 1
    for i in range(1,n):
        fib.append(fib[i]+fib[i-1])
    return fib[-1]

n = int(input())
print(calc_fib(n))
