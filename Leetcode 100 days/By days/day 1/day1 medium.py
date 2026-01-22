class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        s=len(nums)
        mid= s//2
        while mid>0 or mid<s:
            print(mid)
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                mid=mid/2
            else:
                mid=s//2
        return False





s = Solution()
print(s.searchRange([2,5,6,0,0,1,2],0))