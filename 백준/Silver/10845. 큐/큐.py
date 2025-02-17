import sys
from collections import deque as q

que = q([])
inputs = sys.stdin.read()
cmds = inputs.splitlines()
n = int(cmds[0])

output = []
for i in range(1, n+1):
    command = cmds[i].split()
    if command[0] == "push":
        que.append(int(command[-1]))
    elif command[0] == "top":
        if not len(que) == 0:
            output.append(str(que[-1]))
        else:
            output.append("-1")
    elif command[0] == "pop":
        if not len(que) == 0:
            output.append(str(que.popleft()))
        else:
            output.append("-1")
    elif command[0] == "size":
        output.append(str(len(que)))
    elif command[0] == "empty":
        if que:
            output.append("0")
        else:
            output.append("1")
    elif command[0] == "front":
        if not que:
            output.append("-1")
        else:
            output.append(str(que[0]))
    elif command[0] == "back":
        if not que:
            output.append("-1")
        else:
            output.append(str(que[-1]))

sys.stdout.write("\n".join(output)+"\n")