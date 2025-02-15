target = list(map(int, input().split()))
is_asc = sorted(target)
is_des = sorted(target, reverse=True)

if target==is_asc:
    print("ascending")
elif target == is_des:
    print("descending")
else:
    print("mixed")