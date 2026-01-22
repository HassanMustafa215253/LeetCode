class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    count=0
    value=0
    while l1!=None:
        value+=l1.val*pow(10,count)
        l1=l1.next
        count+=1
    s=count
    count =0
    while l2!=None:
        value+=l2.val*pow(10,count)
        l2=l2.next
        count+=1
    if count>s:
        s=count

    global get
    get=ListNode(value%10)
    temp=get
        
    for i in range(s-1,0,-1):
        value=int(value/10)
        print(value%10) 
        temp.next=ListNode(value%10)
        temp=temp.next

    return get

    print(value)
    while get!=None:
        print(get.val,end="")
        get=get.next


l1=ListNode(2,ListNode(4,ListNode(3)))
l2=ListNode(5,ListNode(6,ListNode(4)))

addTwoNumbers(l1,l2)