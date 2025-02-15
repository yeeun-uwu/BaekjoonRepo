ans = []

for i in range(10):
    ans.append(int(input()) % 42)

ans_t = set(ans)
print(len(ans_t))