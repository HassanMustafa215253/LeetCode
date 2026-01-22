class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s=set(nums)
        if len(s)== len(nums):
            return False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i ==j:
                    continue
                if nums[i] == nums[j] and abs(i-j)<=k:
                    return True
        return False


s = Solution()
print(s.containsNearbyDuplicate([1,0,1,1],1))
