import sys as s

m = int(s.stdin.readline().strip())
#cmd = [s.stdin.readline().strip().split() for _ in range(m)]
#메모리제한때매 매번 받는걸로 수정정

sss = set() #집합
output = s.stdout.write #빠르게출력하기위해서서

for _ in range(m):
    i = s.stdin.readline().strip().split()

    if i[0] == "add":
        if not int(i[1]) in sss:
            sss.add(int(i[1]))
    elif i[0] == "remove":
        if int(i[1]) in sss:
            sss.discard(int(i[1]))
    elif i[0] == "check":
        if int(i[1]) in sss:
            output("1\n")
        else:
            output("0\n")
    elif i[0] == "toggle":
        if int(i[1]) in sss:
            sss.discard(int(i[1]))
        else:
            sss.add(int(i[1]))
    elif i[0] == "all":
        sss = set(range(1, 21))
    else:
        sss.clear()