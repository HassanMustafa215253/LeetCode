class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        s=len(nums)-1
        r=[]
        print(s)
        for i in range(1,s+1):
            r.clear()
            sum=0
            print("i = ",i)
            print("initial")
            for x in range(0,i+1):
                r.append(nums[x])
                sum+=nums[x]
                print("x= ",x)
                print("r= ", r )
                print("s = ", sum ,"\n")
            print("Loop j")
            if i == s:
                if sum==0:
                    return True
                if sum%k==0:
                    return True
                continue
            for j in range(i+1,s+1):
                print("S+1 = ",s+1)
                print("j = ",j)
                print("r = ",r)
                print("sum = ",sum)

                if sum==0:
                    return True
                if sum%k==0:
                    return True
                sum-=r[0]
                sum+=nums[j]
                print("r = ",r[0])
                print("nums[j] = ",nums[j])
                print("sum after = ",sum)
                r.pop(0)
                r.append(nums[j])
                if j == s:
                    if sum==0:
                        return True
                    if sum%k==0:
                        return True
                    continue
            print("")
        return False


s=Solution()
print(s.checkSubarraySum([1,2,3],5))