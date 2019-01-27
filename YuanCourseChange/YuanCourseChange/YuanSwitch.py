import random

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

def choseReplaceInd(mode):
    global replaceInd, replaceNum
    for i in range(mode*2, mode*2+2):
        #print(aval[course.index(i)])
        #print(node in final[course[i]])
        if node in aval[i]:#final[course[i]]:
            replaceInd = i
            replaceNum = course[i]
            break

def process(cur):
    result = []
    for i in aval[course.index(cur)]: #final[cur] = aval[course.index[cur]]
        if i != cur or visited[course.index(cur)]==False:
            result.append(i)
    return result

#assigning previous node, connect nodes i connect from v
def prev(v,i):
    previous[i] = v

#perform breath first search to find ways to swap and insert the course into avaliable place
def change(ind,node):
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
                    visited[course.index(v)] = True #set the parent visited
                    if not visited[course.index(i)] : #prevent visiting a node twice
                        tree[course.index(i)] = course.index(v) #create directed edge from child to parent
                        visited[course.index(i)] = True #set the child visited
                        if(node in aval[course.index(i)] and leafInd == None): #if the leaf is found, then set
                            leafInd = course.index(i)
                        queue += process(i) #add more child to queue
                       
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
    while i != tree[i]:
        swapInst.append(i)
        #print("i",i)
        i = tree[i]
    swapInst.append(i)
    if(changeInd != swapInst[-1]):
        swapInst.append(changeInd)
    return
def testCorrect(courseCopy,aval):
    for i in range(len(courseCopy)):
        if not courseCopy[i] in aval[i]:
            return False
    return True

def changeCourse(course,aval,changeInd, node, mode):
    global previous, visited, leafInd, swapInst, tree
    tree = [i for i in range(len(course))]
    visited = [False for _ in range(len(course))]
    leafInd = None
    swapInst = []
    courseCopy = [course[i] for i in range(len(course))]
    #print("course", course)
    #print("aval", aval)
    replaceInd = None
    replaceNum = None
    final = dict(zip(courseCopy,aval))
    #print("initial course", course)

    choseReplaceInd(mode)
    #print("replaceInd:", replaceInd,"replaceNum:", replaceNum)

    change(changeInd,replaceNum)
    #print("leaf",leafInd)
    
    if leafInd != None and replaceNum != None:
        course[changeInd] = replaceNum
        traverse(leafInd)
        leafInd = None
        j = 1
        while j < len(swapInst):
            course = swap(course, swapInst[0],swapInst[j])
            j+=1
        course[replaceInd] = node
    return courseCopy
    print("modified course",courseCopy)
    

course = []
aval = []
success = 0
iteration = 20
for i in range(iteration):
    testGenerator(8)
    changeInd = random.randrange(0,8)
    node = course[changeInd]
    print("ChangeInd:",changeInd)
    mode = random.randrange(0,4) # 0 = switch to morning first semester 1 = switch to afternoon first semester, 2 = switch to second semester morning, 3 = switch to second semester afternoon
    print("ChangeInd:",changeInd, "mode:",mode)
    courseCopy = changeCourse(course,aval,changeInd, node, mode)
    if testCorrect(courseCopy,aval):
        success+=1
if success == iteration:
    print("success")
