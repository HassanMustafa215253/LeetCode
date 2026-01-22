class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        words = sentence.split()
        dictionary.sort()
        for i, word in enumerate(words):
                for d in dictionary:
                    if word.startswith(d):
                        words[i] = d
                        break
        return ' '.join(words)
            
s=Solution()
print(s.replaceWords(["catt","cat","bat","rat"],"the cattle was rattled by the battery"))