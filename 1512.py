import math
def numIdenticalPairs(nums: list[int]) -> int:
    d={}
    for i in nums:
        print(i)
        if i in d:
            d[i]=1
        else:
            return True
    return False

print("\nfinal: ",numIdenticalPairs([1,2,3,4]))