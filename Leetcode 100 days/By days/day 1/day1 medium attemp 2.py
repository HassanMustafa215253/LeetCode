class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        try:
            left = nums.index(target)
            right = len(nums) - 1 - nums[::-1].index(target)
            return [left, right]
        except ValueError:
            return [-1,-1]
        en