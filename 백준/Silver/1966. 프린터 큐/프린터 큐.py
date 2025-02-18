import sys
from collections import deque as dq

def calc(n, m, pri):
    prio = dq(pri)
    doc = dq([_ for _ in range(n)]) 
    cnt = 0

    while doc: 
        print_flag = True 

        for i in range(1, len(prio)):
            if prio[0] < prio[i]:
                print_flag = False
                break

        if print_flag:
            printed = doc.popleft()  
            prio.popleft()  
            cnt += 1
            if printed == m:  
                return cnt
        else:
            not_printed = doc.popleft()  
            not_prio = prio.popleft()  
            doc.append(not_printed) 
            prio.append(not_prio)  

t = int(sys.stdin.readline().strip())
for i in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    priority = list(map(int, sys.stdin.readline().strip().split()))
    print(calc(n, m, priority))