class Solution:
    def isNStraightHand(self, hand: list[int], size: int) -> bool:
        s=len(hand)
        if s%size!=0:
            return False
        hand.sort()
        for i in range(int(s/size)):
            t=[0]*size
            t[0]=hand[0]
            for x in range(size-1):
                e=t[x]
                if e+1 in hand:
                    t[x+1]=e+1
                    hand.remove(e+1)
                else:
                    return False
            hand.remove(hand[0])
        return True



s=Solution()

print(s.isNStraightHand([8,8,9,7,7,7,6,7,10,6],2))