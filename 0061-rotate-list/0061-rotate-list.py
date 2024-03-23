# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        l=[]
        t=head
        while t:
            l.append(t.val)
            t=t.next
        k=k%len(l)
        x=l[len(l)-k:]+l[:len(l)-k]
        h=ListNode(x[0])
        m=h
        for i in range(1,len(x)):
            t=ListNode(x[i])
            m.next=t  #linking
            m=t
        return h