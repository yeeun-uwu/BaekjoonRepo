n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    members.append((int(age), name, i))

members.sort(key = lambda x:(x[0], x[-1]))
for i in members:
    print(*i[:-1])