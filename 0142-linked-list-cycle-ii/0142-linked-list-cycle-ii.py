# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        t=head
        while t:
            if t in s:
                return t
            s.add(t)
            t=t.next
        return None