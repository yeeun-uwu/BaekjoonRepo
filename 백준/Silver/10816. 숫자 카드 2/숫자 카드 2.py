n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))



nums_dict = {}

for i in numbers:
    if i in nums_dict:
        nums_dict[i] += 1
    else:
        nums_dict[i] = 1    

ans = [nums_dict.get(i, 0) for i in targets]

print(*ans)