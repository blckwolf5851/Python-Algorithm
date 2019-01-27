# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    #text = sys.stdin.read()
    text = input()
    success = 0
    fail = 0
    failind = None
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append([next,i])

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                fail += 1
                failind = i +1
                print(failind)
                break
                
            else:
                top = opening_brackets_stack.pop()
                if top[0] == '(' and next == ')' or top[0] == '[' and next == ']' or top[0] == '{' and next[0] == '}':
                    success += 1
                else:
                    fail += 1
                    failind = i + 1 #next is not int
                    print(failind)
                    break
        if fail > 0:
            break
    # Printing answer, write your code here
    if len(opening_brackets_stack) > 0 and failind == None:
        print(opening_brackets_stack[-1][-1]+1)
    elif len(opening_brackets_stack) == 0 and failind == None:
        print('Success')
