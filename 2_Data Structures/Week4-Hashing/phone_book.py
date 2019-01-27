# python3
import random
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))



def addPhone(contact,phoneNum,name,p,a,b,m):
    for i in contact[((a * phoneNum + b) % p) % m]:
        if i[0] == phoneNum:
            i[1] = name
            return
    contact[((a * phoneNum + b) % p) % m].append([phoneNum,name])

def find(p,a,b,m,phoneNum,contact):
    ind = ((a * phoneNum + b) % p) % m
    for i in contact[ind]:
        if i[0] == phoneNum:
            return i[1]
    return "not found"

def delete(p,a,b,m,phoneNum,contact):
    ind = ((a * phoneNum + b) % p) % m
    for i in contact[ind]:
        if i[0] == phoneNum:
            contact[ind].pop(i)
            return

def process_queries(queries):
    result = []
    m = 1000
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [[-1]] * m
    p= 10000019
    a = random.randrange(1,p)
    b = random.randrange(1,p)
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            addPhone(contacts,cur_query.number,cur_query.name,p,a,b,m)
        elif cur_query.type == 'del':
            delete(p,a,b,m,cur_query.number,contacts)
        else:
            result.append(find(p,a,b,m,cur_query.number,contacts))
    return result
    

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

