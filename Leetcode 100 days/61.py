class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotateRight(head: ListNode, k: int):
    if k ==0 or head==None or head.next==None:
        return head
    a=[]
    front=head
    back=head
    l=1
    end=None
    while k!=0:
        if front.next==None:
            print("None found")
            end=front
            front=head
            k-=1
            k=k%l
        else:
            l+=1
            k-=1
            front=front.next
        print("k= ",k)
        print("l= ",l)
        print("front.val= ",front.val)
    while front.next!=None:
        back=back.next
        front=front.next
    front.next=head
    temp=back.next
    back.next=None
    run=temp
    while run!=None:
        run=run.next
    return temp

head=ListNode(1,ListNode(2,ListNode(3)))
head=rotateRight(head,2000000000)
while(head!=None):
    print(head.val,end=" ")
    head=head.next