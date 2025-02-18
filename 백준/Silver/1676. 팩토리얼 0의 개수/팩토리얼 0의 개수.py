import math

def fac_0(n):
    num = math.factorial(n)
    nums = list(map(int, list(str(num))))
    nums = nums[::-1]
    cnt = 0
    for i in nums:
        if i == 0:
            cnt += 1
        else: 
            break

    return cnt

n = int(input())
print(fac_0(n))