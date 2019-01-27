# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pivot = a[l]
    L = l
    i = l
    R = r
    while i <= R:
        if a[i] == pivot:
            i += 1
        elif a[i] < pivot:
            a[i],a[L] = a[L],a[i]
            L += 1
            i += 1
        else:
            a[i],a[R] = a[R], a[i]
            R -= 1
        ind = [L,R]
    return ind



def randomized_quick_sort(a, l, r):
    if l >= r:
        return 
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1)
    randomized_quick_sort(a, m[1] + 1, r)
    return a


n = int(input())
inp = input()
a = [int(x) for x in inp.split()]
stri = ''
stri += str(randomized_quick_sort(a, 0, n-1)[0])
for i in randomized_quick_sort(a, 0, n-1)[1:]:
    stri += ' '+ str(i)
print(stri)