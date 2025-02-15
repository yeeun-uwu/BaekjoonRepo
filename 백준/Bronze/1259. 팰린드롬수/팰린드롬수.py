def is_Palin(n):
    l = list(str(n))
    palin = True
    for i in range(len(l) // 2):
        if l[i] == l[len(l)-i-1]:
            pass
        else:
            palin = False
            break

    return palin

while True:
    numbers = int(input())
    if numbers == 0:
        break

    if is_Palin(numbers):
        print("yes")
    else:
        print("no")
    