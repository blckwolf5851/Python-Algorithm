#input format: items [[weight,value] [weight,value]...]

def dynamicKnapsack(W,item):
    init = [[0 for x in range(W+1)] for i in range(len(item)+1)] # set matrix: total capacity * len(item)
    
    for i in range(1,len(item)+1): # i = row
        for j in range(1,W+1):#j = colum
            init[i][j] = init[i-1][j] # set initial biggest value on the node
            if item[i-1][0] <= j: # if the current weight of the bag bigger equal than current item
                val = init[i-1][j-item[i-1][0]] + item[i-1][1]
                if val > init[i][j]: #replace the biggest value
                    init[i][j] = val
    # optimal value = init[-1][-1]
    for i in init:
        print(i)
    return init

def traceback(i,j,item): # i = len(item)   j = W
    global gives
    init = dynamicKnapsack(W,item)
    #base case
    if i<= 0 and j <= 0:
        return 
    if init[i][j] == init[i-1][j]:
        gives[i-1] = 0
        traceback(i-1,j,item)
    elif init[i][j] == init[i-1][j-item[i-1][0]] + item[i-1][1]:
        gives[i-1] = 1
        traceback(i-1,j-item[i-1][0],item)

item = [[6,30],[3,14],[4,16],[2,9]]
W = 10
gives = [0 for i in range(len(item))]
traceback(len(item),W,item)
for i in range(len(gives)):
    if gives[i]== 1:
        print(item[i])
print(gives)
