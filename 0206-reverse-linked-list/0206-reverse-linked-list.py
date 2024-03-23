# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        l=[]
        while t:
            l.append(t.val)
            t=t.next
        x=head
        i=0
        while x:
            x.val=l.pop()
            x=x.next
        return head