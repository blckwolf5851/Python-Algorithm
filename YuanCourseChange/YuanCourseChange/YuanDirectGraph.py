import random
iter = 0
def testGenerator(courseNum):
    global course, aval
    randCourse = [str(i+1) for i in range(courseNum)]
    random.shuffle(randCourse)
    course = randCourse
    aval = [[] for _ in range(courseNum)]
    for i in range(courseNum):
        aval[i].append(str(randCourse[i]))
        #print("pass1")
        for j in range(random.randint(1,4)):
            rand = random.randint(1,courseNum+5)
            while str(rand) in aval[i]:
                #print("pass2")
                rand = random.randint(1,courseNum+5)
            aval[i].append(str(rand))
    print("course:",course)
    print("aval:",aval)

def process(cur):
    result = []
    for i in aval[course.index(cur)]: #final[cur] = aval[course.index[cur]]
        if i != cur or visited[course.index(cur)]==False:
            iter+=1
            result.append(i)
    return result

#perform breath first search to find ways to swap and insert the course into avaliable place
#build directed graph of bottom to top
def change(ind):
    global leafInd
    cur = course[ind]
    visited = [False for _ in range(len(course))]
    queue = [cur]
    end = False
    while queue and end == False:
        #print("queue", queue)
        v= queue.pop(0)
        if v in course:
            #print("v",v)
            for i in process(v):
                if i in course:
                    iter+=1
                    visited[course.index(v)] = True #set the parent visited
                    if not visited[course.index(i)] : #prevent visiting a node twice
                        tree[course.index(i)] = course.index(v) #create directed edge from child to parent
                        visited[course.index(i)] = True #set the child visited
                        if(node in aval[course.index(i)] and leafInd == None): #if the leaf is found, then set
                            leafInd = course.index(i)
                        queue += process(i) #add more child to queue

def swap(course, ind1,ind2):
    temp = course[ind1]
    course[ind1] = course[ind2]
    course[ind2] = temp
    return course


def traverse(i):
    #swapInst.append(i)
    while i != tree[i]:
        swapInst.append(i)
        #print("i",i)
        i = tree[i]
    swapInst.append(i)
    if(changeInd != swapInst[-1]):
        swapInst.append(changeInd)
    return

#test the correctness of the resulting courses
def testCorrect(courseCopy,aval):
    for i in range(len(courseCopy)):
        if not courseCopy[i] in aval[i]:
            return False
    return True

def changeCourse(course,aval,changeInd, node):
    global previous, visited, leafInd, swapInst, tree
    tree = [i for i in range(len(course))]
    visited = [False for _ in range(len(course))]
    leafInd = None
    swapInst = []
    courseCopy = [course[i] for i in range(len(course))]
    #print("course", course)
    #print("aval", aval)

    final = dict(zip(courseCopy,aval))
    
    change(changeInd)
    if leafInd != None:
        courseCopy[changeInd] = node
        traverse(leafInd)

    j = 1
    while j < len(swapInst):
        courseCopy = swap(courseCopy, swapInst[0],swapInst[j])
        j+=1

    print("modified course",courseCopy)
    return courseCopy
    #print(leafInd)
    #print(tree)

course = []
aval = []
success = 0
iteration = 1

for i in range(iteration):
    courseLen = 8
    changeInd =random.randrange(0,courseLen)
    node = str(random.randrange(1,courseLen+5))

    testGenerator(courseLen)
    print("change", course[changeInd], "to", node)
    courseCopy = changeCourse(course,aval,changeInd, node)
    if testCorrect(courseCopy,aval):
        success+=1
if success == iteration:
    print("success")
