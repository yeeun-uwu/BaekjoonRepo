n, m = map(int, input().split())
nnn = set()
mmm = set() #n 집함이랑 m 집합

for i in range(n):
    nnn.add(input())

for i in range(m):
    mmm.add(input())

ans = nnn.intersection(mmm) #교집합
ansss= list(ans)
ansss.sort()

print(len(ansss))
for i in ansss:
    print(i)