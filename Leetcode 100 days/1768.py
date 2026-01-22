def mergeAlternately(word1: str, word2: str) -> str:
    w1=len(word1)
    w2=len(word2)
    a=[0]*(min(w1,w2)*2)
    p=0
    for i in range(min(w1, w2)):
        print("p: ",p)
        a[p]=word1[i]
        a[p+1]=word2[i]
        p+=2
    print(a)
    a="".join(a)
    print(p)
    print(p//2)
    if w1>p//2:
        a+=word1[p//2:]
    elif w2>p//2:
        print(word2[p//2:])
        a+=word2[p//2:]
    return a
print(mergeAlternately("abc","pqrstu"))