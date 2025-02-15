
r = 31
m = 1234567891

def hashing(l):
    let = list(l)
    h = 0
    p = 1
    for i in range(len(let)):
        char_v = ord(let[i]) - ord('a') + 1
        h = (h + char_v * p) % m
        p = (p * r) % m 

    return h

n = int(input())
target = input()
print(hashing(target))