n = int(input())
houses = list(map(int, input().split()))
houses.sort()

if n % 2 == 1:
    print(houses[n//2])
else:
    print(houses[n//2 - 1])