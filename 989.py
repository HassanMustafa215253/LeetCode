class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=str(k)
        for i in range(len(s)):
            l=len(num)
            if i <l:
                num[-1-i]+=int(s[-1-i])
                for j in range(i,l):
                    if num[-1-j]>=10:
                        num[-1-j]-=10
                        if 2+j>l:
                            num.insert(0,1)
                        else:
                            num[-2-j]+=1
            else:
                num.insert(0,int(s[-i-1]))
        return num