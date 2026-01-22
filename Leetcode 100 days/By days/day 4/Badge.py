class Solution:
    def longestPalindrome(self, s: str) -> int:
        f=False
        c=0
        a=set()
        b=set(s)
        for i in s:
            if i in a:
                continue
            else:
                a.add(i)
            j=s.count(i)
            if j%2==0:
                c+=j
            else:
                f=True
                c+=j-1
            if b==a:
                break
        if len(a)==1:
            print("There")
            return len(s)
        if f==0:
            print("asd")
            return c
        print("Here")
        return c+1
    
s=Solution()
print(s.longestPalindrome("ababababa"))