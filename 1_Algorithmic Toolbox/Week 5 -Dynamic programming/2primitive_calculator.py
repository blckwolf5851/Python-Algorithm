# Uses python3
import sys
import math
#
def optimal_sequence(n):
    dyn = [[0]]
    for i in range(1,n+1):
        minLen = math.inf
        minInd = math.inf
        if i % 3 == 0:
            nums = dyn[i//3]
            minLen = len(nums)
            minInd = i//3
        elif i % 2 == 0:
            nums = dyn[i//2]
            minLen = len(nums)
            minInd = i//2

        minus = dyn [i - 1]
        if len(minus) < minLen:
            minLen = len(minus)
            minInd = i - 1
        dyn.append([x for x in dyn[minInd]])
        dyn[i].append(i)

        if i >= 3 and i // 3 > 0:
            dyn[i//3 - 1] = None
        minLen = math.inf
        minInd = math.inf
    if dyn[-1][0] == 0:
        del dyn[-1][0]
    return dyn[-1]

def dynamic_sequence(n):
    operations_count = [0] * (n + 1)

    operations_count[1] = 1
    for i in range(2, n + 1):
        count_index = [i - 1]
        if i % 2 == 0:
            count_index.append(i // 2)
        if i % 3 == 0:
            count_index.append(i // 3)

        min_count = min([operations_count[x] for x in count_index])
        operations_count[i] = min_count + 1

    current_value = n
    value_trail = [current_value]
    while current_value != 1:
        option_list = [current_value - 1]
        if current_value % 2 == 0:
            option_list.append(current_value // 2)
        if current_value % 3 == 0:
            option_list.append(current_value // 3)

        current_value = min(
            [(c, operations_count[c]) for c in option_list],
            key=lambda x: x[1]
        )[0]
        value_trail.append(current_value)
    return reversed(value_trail)



#input = sys.stdin.read()
n = int(input())
str1 = ''
sequence = optimal_sequence(n)
print(len(sequence)-1)
for x in sequence:
    str1 += str(x) + ' '
print(str1)
