def dissum(m):

    return sum(int(digit) for digit in str(m))

n = int(input())

for i in range(max(1, n-len(str(n))*9), n-len(str(n))):
    if dissum(i) + i == n:
        print(i)
        exit(0)
print(0)