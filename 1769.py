def minOperations( boxes: str) -> list[int]:
    s=len(boxes)
    l=[0]*s
    for i in range(s):
        for j in range(0,i):
            if boxes[j] == '1':
                l[i] += i-j
        for j in range(s-1,i,-1):
            if boxes[j] == '1':
                l[i] += j-i
    return l
print(minOperations("001011"))