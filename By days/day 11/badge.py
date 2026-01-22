class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        d={}
        res=[0]*len(arr1)
        ind=0
        for i in arr1:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        print(d)
        for i in arr2:
            print("i = ",i)
            for j in range(d[i]):
                print("d[i] = ",d[i])
                res[ind]=i
                ind+=1
            del d[i]
        for i,count in sorted(d.items()):
            for j in range(count):
                res[ind]=i
                ind+=1
        return res

s=Solution()
print(s.relativeSortArray([28,6,22,8,44,17],[22,28,8,6]))
