#uses python3
def knap(W,change):
    init = [[0 for i in range(W+1)] for i in range(len(change)+1)]
    for i in range(len(change)+1):
        for j in range(W+1):
            init[i][j] = init[i-1][j]
            if j >= change[i-1]:
                val = init[i-1][j-change[i-1]] + change[i-1]
                if val > init[i][j]:
                    init[i][j] = val
    return init[-1][-1]

def optimal_weight(W, w):
    items = [0]
    for item in w:
        if item <= W:
            items.append(item)

    item_length = len(items)
    capacity = W + 1

    weights = [[0 for _ in range(item_length)] for _ in range(capacity)]

    for j in range(1, item_length):
        for i in range(1, capacity):
            previous = weights[i][j - 1]
            current = items[j] + weights[i - items[j]][j - 1]
            if current > i:
                weights[i][j] = previous
            else:
                weights[i][j] = max(previous, current)

    return weights[-1][-1]

inp1 = input()
inp2 = input()
W = int(inp1.split()[0])
change = [int(x) for x in inp2.split()]
print(optimal_weight(W,change))
