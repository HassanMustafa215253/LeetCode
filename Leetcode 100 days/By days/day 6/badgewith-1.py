class Solution:
    def isNStraightHand(self, hand: list[int], size: int) -> bool:
        s=len(hand)
        print("s = ",s)
        if s%size!=0:
            return False
        sd=int(s/size)
        print("sd = ",sd,"\n")
        for i in range(sd):
            t=[-1]*size
            print("hand = ", hand)
            print("hand[0] = ", hand[0])
            d=0
            while t[0]==-1:
                t[0]=hand[d]
                d+=1
            d=0
            print("t = ",t,"\n")
            for x in range(size-1):
                e=t[x]
                print("t = ",t)
                print("t x+1 = ",t[x]+1)
                print("t x+1 = ",t[x]-1)
                print("hand = " , hand,"\n")

                if e+1 not in hand:
                    return False
                else:
                    t[x+1]=e+1
                    print("Removing : ",e+1)
                    hand[hand.index(e+1)]=-1
            print("Removing [0] : ",hand[0],"\n")
            hand.remove(t[0])
        return True


s=Solution()

print(s.isNStraightHand([2,1],2))