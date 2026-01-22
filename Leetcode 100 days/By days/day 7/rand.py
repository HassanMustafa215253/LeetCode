class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        high=len(nums)-1
        low=0
        while low<=high:
            mid=(low+high)//2
            print(nums[mid])
            if nums[mid] == target :
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return low
s=Solution()
print(s.searchInsert([4,5,6,7,0,1,2],0))