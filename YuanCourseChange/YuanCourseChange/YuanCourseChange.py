import random
#test1
#course = ["3","4","1","2"]
#aval = [["1", "3"],[ "2", "4", "6"],["1","2","4"],["1","2","3"]]

#test2
#course = ["3","2","1","4"]
#aval = [["2", "3"],[ "1","2", "3", "6"],["1","3","4"],["1","2","4"]]

#test3
#course = ["3","2","1","4"]
#aval = [["3", "1","2","4"],[ "1","2", "3", "6"],["1","2"],["3","2","4"]]

#test4
#course = ["1","2","4","3"]
#aval = [["2", "1"],[ "2", "3","1"],["1","4"],["2","3"]]

def testGenerator(courseNum):
    global course, aval
    randCourse = [str(i+1) for i in range(courseNum)]
    random.shuffle(randCourse)
    course = randCourse
    aval = [[] for _ in range(courseNum)]
    for i in range(courseNum):
        aval[i].append(str(randCourse[i]))
        print("pass1")
        for j in range(random.randint(1,4)):
            rand = random.randint(1,courseNum)
            while str(rand) in aval[i]:
                print("pass2")
                rand = random.randint(1,courseNum)
            aval[i].append(str(rand))
    print("course:",course)
    print("aval:",aval)



#calculate node adjacent
def process(cur):
    result = []
    for i in final[cur]: #final[cur] = aval[course.index[cur]]
        if not i == cur:
            result.append(i)
    return result

#assigning previous node, connect nodes i connect from v
def prev(v,i):
    previous[i] = v

#perform breath first search to find ways to swap and insert the course into avaliable place
#build directed graph of bottom to top
def change(ind):
    global leafInd
    cur = course[ind]
    visited = [False for _ in range(len(course))]
    queue = [cur] #1,3,4
    end = False
    print(queue)
    #print(ifInclude(node,final[cur]))
    if node in final[cur]:#final[cur] = aval[course.index[cur]]    #ifInclude(node,final[cur]):
        leafInd = ind
        end = True

    
    lastI = None
    curV = None
    while queue and end == False:
        print("queue", queue)
        v= queue.pop(0) # 1,3
        
        if v in course:
            print("v",v)
            for i in process(v):
                if i in course:
                    visited[course.index(v)] = True
                    if not visited[course.index(i)] :
                        print("curV vs. v", curV, v)
                        print("lastI vs. i:",lastI, i)
                        print("check leaf of key", v, "node", node , "in" ,final[v], node in final[v])
                        if v != curV and curV != None:
                            prev(course.index(lastI),course.index(v))
                            print("connect", lastI,"to", v)
                        if node in final[v]: #final[v] = aval[course.index[v]]
                            leafInd = course.index(v)    
                            end = True
                            break
                        queue += process(i)
                        visited[course.index(i)] = True
                        lastI = i
                        curV = v
                        prev(course.index(v),course.index(i))
                        print("connect", i,"to", v)
                        print("previous",previous)
                        #print("check leaf of key", i, "node", node , "in" ,final[i], ifInclude(node,final[i]))
                        if node in final[i]: #final[i] = aval[course.index[i]]
                            leafInd = course.index(i)    
                            end = True
                            break
                    #curV = v
    #if not end: #meaning that 
                       
#perform swap function
def swap(course, ind1,ind2):
    temp = course[ind1]
    course[ind1] = course[ind2]
    course[ind2] = temp
    return course

#store a path from root to right leaf into swapInst array, instruction for later manipulating the order of the courses
#uses the find method in data structure: disjoint set
def traverse(i):
    #swapInst.append(i)
    while i != previous[i]:
        swapInst.append(i)
        #print("i",i)
        i = previous[i]
    swapInst.append(i)
    if(changeInd != swapInst[-1]):
        swapInst.append(changeInd)
    return

def testCorrect(courseCopy,aval):
    for i in range(len(courseCopy)):
        if not courseCopy[i] in aval[i]:
            return False
    return True
            

def changeCourse(course,aval,changeInd, node):
    global previous, visited, leafInd, swapInst, final
    #path = [course[i] for i in range(len(course))]
    previous = [i for i in range(len(course))]
    visited = [False for _ in range(len(course))]
    leafInd = None
    swapInst = []
    courseCopy = [course[i] for i in range(len(course))]
    print("course", course)
    print("aval", aval)

    final = dict(zip(courseCopy,aval))
    
    change(changeInd)
    print("leaf",leafInd)
    previous[changeInd] = changeInd # prevent infinit loop
    #print(previous)
    print("previous",previous)
    if leafInd != None:
        courseCopy[changeInd] = node
        traverse(leafInd)

    j = 1
    print("swap int", swapInst)
    while j < len(swapInst):
        courseCopy = swap(courseCopy, swapInst[0],swapInst[j])
        j+=1

    print("modified course",courseCopy)
    print("Correctness:",testCorrect(courseCopy,aval))

course = ['1', '6', '7', '4', '2', '5', '3', '8']
aval = [['1', '6', '5', '8'], ['6', '2', '7', '8'], ['7', '3'], ['4', '5', '6'], ['2', '1', '8', '4'], ['5', '1', '2', '6'], ['3', '8', '7', '1'], ['8', '5']]
courseLen = 8
changeInd = 0#random.randrange(0,courseLen)
node = "4"#str(random.randrange(1,courseLen))

#testGenerator(courseLen)
print("change", course[changeInd], "to", node)
changeCourse(course,aval,changeInd, node)
