# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None :
            return None
        if head==None:
            return head
        s=head
        f=head
        while f!=None and f.next!=None:
            s=s.next
            f=f.next.next
        x=head
        while x:
            if x.next==s:
                break
            x=x.next
        x.next=s.next
        return head
                