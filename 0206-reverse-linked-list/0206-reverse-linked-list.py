# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=None
        temp=head
        while temp:
            f=temp.next
            temp.next=p
            p=temp
            temp=f
        return p