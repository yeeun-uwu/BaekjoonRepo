import sys

def calc(nums):
    if len(nums)==0: return 0

    nums.sort()
    delete = int((len(nums) * 0.15)+0.5)

    if delete> 0:
        nums = nums[delete:-delete]
    
    s = sum(nums)
    return int((s/len(nums))+0.5) if nums else 0 

n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

print(calc(nums))