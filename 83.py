# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    l1s=""
    l2s=""

    temp1=l1
    temp2=l2
    while temp1 or temp2 :
        if temp1!=None:
            l1s+=str(temp1.val)
            temp1=temp1.next
        if temp2!=None:
            l2s+=str(temp2.val)
            temp2=temp2.next

    summ=str(int(l1s[::-1])+int(l2s[::-1]))
    print(summ)
    temp=l1
    prev=l1
    for i in summ:
        if temp!=None:
            temp.val=int(i)
        else:
            temp=ListNode(val=int(i), next=None)
            prev.next=temp
        print(temp.val)
        prev=temp
        temp=temp.next
    temp=None
    return l1

l2=ListNode(2,ListNode(4,ListNode(9)))
l1=ListNode(5,ListNode(6,ListNode(4,ListNode(9))))
l1=addTwoNumbers(l1,l2)
print("\n\n printing result")
while(l1):
    print(l1.val)
    l1=l1.next