# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s={}
        t=head
        i=0
        while t:
            if t in s:
                return t
            s[t]=i
            i+=1
            t=t.next
        return None