# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        t=headB
        while t:
            s.add(t)
            t=t.next
        t=headA
        while t:
            if t in s:
                return t
            t=t.next
        return None