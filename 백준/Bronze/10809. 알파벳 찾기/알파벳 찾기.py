import string

s = input()

targets = list(string.ascii_lowercase)
ans = []

for i in targets:
    ans.append(s.find(i))

print(*ans)