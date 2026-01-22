import math
from collections import Counter
def majorityElement(nums: list[int]) -> int:
    nums = dict(Counter(x for x in nums if x % 2 == 0))
    if not nums:
        return -1
    print(nums)
    maxval = max(nums.values())
    print("maxval:",maxval)
    p=[]
    for i in nums:
        print("i:",i)
        if nums[i] == maxval:
            return i
        else:
            return min(p)

print(majorityElement([0,1,2,2,4,4,1]))