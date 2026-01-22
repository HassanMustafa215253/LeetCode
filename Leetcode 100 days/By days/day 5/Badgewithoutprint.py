class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        sm=set(words[0])
        smi=0
        for i in range(len(words)-1):
            temp=set(words[i+1])
            if len(temp)<len(sm):
                sm=temp
                smi=i
        r=list(words[smi])
        for i in words[smi]:
            if i not in r:
                continue
            for j in range(len(words)):
                if j==smi:
                    continue
                c=r.count(i)
                c2=words[j].count(i)
                if i not in words[j]:
                    for x in range(c-c2):
                        r.remove(i)
                    break
        return r

s=Solution()
print(s.commonChars(["cool","lock","cook"]))