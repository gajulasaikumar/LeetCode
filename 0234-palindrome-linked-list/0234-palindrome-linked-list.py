# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        t=head
        s=[]
        while t:
            s.append(t.val)
            t=t.next
        return s[::-1]==s