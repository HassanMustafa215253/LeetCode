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
                print("\ncontinue\n")
                continue
            for j in range(len(words)):
                if j==smi:
                    continue
                c=r.count(i)
                print ("\nI = ", i)
                print("r = " ,r)
                print ("word[j] = ", words[j])
                if i not in words[j]:
                    print("not found Remove")
                    for x in range(c):
                        r.remove(i)
                    break
                else:
                    print("found Remove")
                    c2=words[j].count(i)
                    print ("c = ", c)
                    print("C2 = " ,c2)
                    if c>c2:
                        for a in range(c-c2):
                            r.remove(i)
                            break
        return r

s=Solution()
print(s.commonChars(["cool","lock","cook"]))