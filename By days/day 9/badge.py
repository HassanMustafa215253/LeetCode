from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        arr=[0]*len(nums)
        arr[0]=1
        sum=0
        mod=0
        r=0
        for i in range(len(nums)):
            sum+=nums[i]%k
            mod=sum%k
            r+=arr[mod]
            arr[mod]+=1
        return r

s=Solution()
print(s.subarraysDivByK([4,5,0,-2,-3,1],5))