class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[]
        inter=list(set(nums1)&set(nums2))
        for num in inter:
            c1=nums1.count(num)
            c2=nums2.count(num)
            if num not in res:
                if c1 and c2:
                    for i in range(min(c1,c2)):
                        res.append(num)

        return res
s=Solution()
print(s.intersection([1,2,2,1],[2,2]))