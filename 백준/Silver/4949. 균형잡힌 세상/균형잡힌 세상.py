#9012 괄호문제 응용해서 해결

from collections import deque as q

def isvps(string):
    things = q([])

    for i in string:
        if i == "(":
            things.append(i)
        elif i == "[":
            things.append(i)
        elif i == ")":
            if not things:
                return "no"
            else:
                a = things.pop()
                if a != "(":
                    return "no"
        elif i == "]":
            if not things:
                return "no"
            else:
                a = things.pop()
                if a != "[":
                    return "no"
        else: continue
    
    if not things:
        return "yes"
    else:
        return "no"

while True:
    string = input()
    if string == ".":
        break
    else:
        print(isvps(string))