class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s=set(nums)
        if len(s)== len(nums):
            return False
        r=[ i for i in s if nums.count(i)>1]
        print("r = ",r)
        for i in r:
            print("i = ",i)
            count=0
            a=nums.index(i)
            print("a = ",a)
            while count<5:
                try:
                    b=(nums[a+1:].index(i))+a+1
                    print("b = ",b)
                    
                    count+=1
                    if abs(a-b)<=k:
                        print(" not chainging")
                        return True
                    else:
                        print("chainging")
                        print("A= ", a)
                        print("B= ", b)
                        a=b
                        print("A= ", a)
                        print("B= ", b)
                except:
                    print("Break")
                    break
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,0,1,1],1))
