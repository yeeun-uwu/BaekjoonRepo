import math, sys
    
m, n = map(int, sys.stdin.readline().split())
prime = [True for i in range(n+1)]
prime[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if prime[i] == True:
        j = 2
        for j in range(i * 2, n+1, i):
            prime[j] = False

for i in range(m, n+1):
    if(prime[i]): print(i)