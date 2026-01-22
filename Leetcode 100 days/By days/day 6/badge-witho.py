class Solution:
    def isNStraightHand(self, hand: list[int], size: int) -> bool:
        s=len(hand)
        print("s = ",s)
        if s%size!=0:
            return False
        sd=int(s/size)
        print("sd = ",sd,"\n")
        for i in range(sd):
            t=[0]*size
            print("hand = ", hand)
            print("hand[0] = ", hand[0])
            t[0]=hand[0]
            print("t = ",t,"\n")
            for x in range(size-1):
                e=t[x]
                print("t = ",t)
                print("t x+1 = ",e+1)
                print("hand = " , hand,"\n")

                if e+1 in hand:
                    t[x+1]=e+1
                    print("Removing : ",e+1)
                    hand.remove(e+1)
                elif e-1 in hand:
                    t[x+1]=e-1
                    print("Removing : ",e-1)
                    hand.remove(e-1)
                else:
                    return False
            print("Removing [0] : ",hand[0],"\n")
            hand.remove(hand[0])
        return True



s=Solution()

print(s.isNStraightHand([8,8,9,7,7,7,6,7,10,6],2))