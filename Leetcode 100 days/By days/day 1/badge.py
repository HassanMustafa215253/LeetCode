class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        for i in range(len(s)-1):
            sum+=ord(s[i])-ord(s[i+1])
        return sum
    
s= Solution
    
s.scoreOfString(s,"hello")