# Uses python3
import sys
def min(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min
def get_change(m):
    #write your code here
    change = [1,3,4]
    dyn = [0]
    count = 0
    for i in range(1,m+1):
        dyn.append(100000000000)
        for n in change:
            if i >= n:
                num = dyn[i-n] + 1
                if num < dyn[i]:
                    dyn[i] = num
        
    return dyn[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
