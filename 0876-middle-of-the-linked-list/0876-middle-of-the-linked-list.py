# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        t=head
        while t:
            c+=1
            t=t.next
        n=c//2 +1
        h=head
        k=0
        while h:
            k+=1
            if k==n:
                return h
            h=h.next