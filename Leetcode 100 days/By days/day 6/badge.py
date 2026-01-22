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
            # ix=[0,size]
            print("hand = ", hand)
            print("hand[0] = ", hand[0])
            t[0]=hand[0]
            print("t = ",t,"\n")
            for x in range(size-1):
                print("t = ",t)
                print("t x+1 = ",t[x]+1)
                print("hand = " , hand,"\n")

                if t[x]+1 not in hand:
                    return False
                else:
                    t[x+1]=t[x]+1
                    print("Removing : ",t[x]+1)
                    hand.remove(t[x]+1)
            print("Removing [0] : ",hand[0],"\n")
            hand.remove(hand[0])
        return True
                # for a in hand:
                #     if(t[x]+1==a):
                #         t[x+1]=a
                #         break


s=Solution()

print(s.isNStraightHand([1,2,3,6,2,3,4,7,8],3))