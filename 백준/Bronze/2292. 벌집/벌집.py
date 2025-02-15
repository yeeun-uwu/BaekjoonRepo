n = int(input())

if n == 1:
    print(1)
    exit(0)

k = 1
while 1 + 3 * k * ( k - 1 ) < n:
    k += 1

print(k)