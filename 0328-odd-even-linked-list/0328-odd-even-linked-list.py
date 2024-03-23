# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        o=head
        e=head.next
        h2=e
        while e!=None and e.next!=None:
            o.next=o.next.next
            e.next=e.next.next
            o=o.next
            e=e.next
        o.next=h2
        return head
        
            
            