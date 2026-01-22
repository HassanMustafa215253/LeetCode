class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        dict={0:-1}
        sum=0
        for i,a in enumerate(nums):
            sum+=a
            mod=sum%k
            if mod not in dict:
                dict[mod]=i
            elif i-dict[mod]>1:
                return True
                
        return False



        
    
s=Solution()
print(s.checkSubarraySum([1,2,12],6))