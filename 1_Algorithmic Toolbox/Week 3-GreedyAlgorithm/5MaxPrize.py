# Uses python3
import sys

def optimal_summands(n):
    summands = [1,2]
    
    if n == 1:
        return 1
    st = ''
    for i in range(n):
        if n - sum(summands) >= summands[-1] + 1:
            summands.append(summands[-1]+1)
        else:
            summands[-1] += n-sum(summands)
    if n == 1:
        return 1
    
    #write your code here
    return summands

n = int(input())
st = ''
if optimal_summands(n) != 1:
    for i in optimal_summands(n):
            st += str(i) + ' '
    print(len(optimal_summands(n)))
    print(st)
else:
    print('1')
    print(optimal_summands(n))
