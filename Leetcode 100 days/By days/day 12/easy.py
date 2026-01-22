import bisect
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        if target >0
        index=bisect.bisect_left(numbers,target)
        for i in range(index):
            for j in range(i,index):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
        if len(numbers)==1:

s=Solution()
print(s.twoSum([2,7,11,15],9))