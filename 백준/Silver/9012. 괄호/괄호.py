from collections import deque as q

def isvps(string):
    vps = q([])

    for i in string:
        if i == "(":
            vps.append(1)
        else:
            if len(vps) == 0:
                return "NO"
            else:
                vps.pop()
    
    if len(vps) == 0:
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    print(isvps(input()))