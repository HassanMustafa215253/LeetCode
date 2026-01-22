class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n%2!=0 and n!=1:
            print("False")
            return False
        for i in range(0,(n//2)+1):
            print(i)
            print(pow(2,i,n))
            if pow(2,i,n)==0:
                return True
        print("fasle2")
        return False




s = Solution()
s.isPowerOfTwo(1)