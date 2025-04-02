
def find_min(remain):
    n = 0
    i = 0

    while True:
        n += 1
        for s in str(n):
            if remain[i] == s and i < len(remain):
                i += 1
                if i>= len(remain):
                    return n

remain = input().strip()
print(find_min(remain))
