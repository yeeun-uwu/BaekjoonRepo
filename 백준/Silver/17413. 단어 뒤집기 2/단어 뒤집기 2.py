from collections import deque as dq

def reverseStr(string_list):
    strs = dq(string_list)

    res = []
    for i in range(len(strs)):
        res.append(strs.pop())

    return "".join(res)

def prob(inputline):
    tri = dq([])
    string = []
    ans = []

    for i in inputline:
        if i == "<":
            if string:
                ans.append(reverseStr(string))
                string = []
            tri.append("<")
            ans.append(i)
        elif i == ">":
            tri.pop()
            ans.append(i)
            string = []
        elif tri:
            ans.append(i)
            continue
        elif i == " ":
            ans.append(reverseStr(string))
            string = []
            ans.append(i)
        else:
            string.append(i)

    if string:
        ans.append(reverseStr(string))
    
    return "".join(ans)

s = input()
print(prob(s))