from sortedcontainers import sortedlist
class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        r=sortedlist(nums)
        