
def maxScore( s: str) -> int:
    high=0
    tcount=0
    for i in range(len(s)):
        if s[i]=='1':
            tcount+= 1
    for i in range(1,len(s)-1):
        count0=0
        count1=0
        for j in range(i):
            if s[j]== '0':
                count0+=1
            else:
                count1+=1
        if high<(tcount-count1)+count0:
            high =(tcount-count1)+count0
    return high


print(maxScore("00"))