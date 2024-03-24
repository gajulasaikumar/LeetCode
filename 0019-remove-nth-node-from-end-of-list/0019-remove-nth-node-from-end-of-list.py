# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        l=[]
        t=head
        while t:
            l.append(t.val)
            t=t.next
        l=l[:len(l)-n]+l[len(l)-n+1:]
        n=ListNode(l[0])
        m=n
        for i in range(1,len(l)):
            t=ListNode(l[i])
            m.next=t
            m=t
        return n
        