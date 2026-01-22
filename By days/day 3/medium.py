class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        s=len(nums)
        if s==1:
            return nums[0]
        for i in range(0,s-1,2):
            print(i)
            if nums[i]-nums[i+1]!=0:
                print(i)
                return nums[i]
        return nums[s-1]
    
s=Solution()
print(s.singleNonDuplicate([1,1,2]))