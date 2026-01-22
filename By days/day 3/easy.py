from pickle import TRUE


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        print(nums)
        nums2=set(nums)
        list(nums2)
        print(nums2)
        if list(nums2)!=nums:
            return True
        else:
            return False

s=Solution()
print(s.containsDuplicate([1,2,3,4]))