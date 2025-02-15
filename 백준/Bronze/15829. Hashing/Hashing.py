import string

letters = list(string.ascii_lowercase)
r = 31
m = 1234567891

def hashing(l):
    let = list(l)
    h = 0
    for i in range(len(let)):
        h += (letters.index(let[i]) + 1) * (r ** i) % m 

    return h

n = int(input())
target = input()
print(hashing(target))