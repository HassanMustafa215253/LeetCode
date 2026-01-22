class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary.sort()
        return dictionary


        return ' '.join(words)
    
s=Solution()
print(s.replaceWords(["catt","cat","bat","rat"],"the cattle was rattled by the battery"))