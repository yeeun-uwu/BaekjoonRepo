a = int(input())
b = int(input())
c = int(input())

ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = str(a*b*c)

for i in ans:
    print(target.count(str(i)))