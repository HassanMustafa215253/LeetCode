class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        s=len(nums)
        if len(nums)%2==0:
            r=nums[k:]
            nums[k:]=nums[:k]
            nums[:k]=r
            print(nums)
        else:
            r=nums[k+1:]
            nums[k:]=nums[:k+1]
            nums[:k]=r
            print(nums)
s=Solution()
print(s.rotate([1,2,3,4,5,6,7],3))