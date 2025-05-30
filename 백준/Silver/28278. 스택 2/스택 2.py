import sys
from collections import deque as q

stack = q([])
inputs = sys.stdin.read()
cmds = inputs.splitlines()
n = int(cmds[0])

output = []
for i in range(1, n+1):
    command = cmds[i].split()
    if command[0] == "1":
        stack.append(int(command[-1]))
    elif command[0] == "5":
        if not len(stack) == 0:
            output.append(str(stack[-1]))
        else:
            output.append("-1")
    elif command[0] == "2":
        if not len(stack) == 0:
            output.append(str(stack.pop()))
        else:
            output.append("-1")
    elif command[0] == "3":
        output.append(str(len(stack)))
    else:
        if stack:
            output.append("0")
        else:
            output.append("1")

sys.stdout.write("\n".join(output)+"\n")