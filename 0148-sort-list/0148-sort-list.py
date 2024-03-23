# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        l=[]
        while t!=None:
            l.append(t.val)
            t=t.next
        l.sort()
        x=head
        i=0
        while x:
            x.val=l[i]
            x=x.next
            i+=1
        return head
        
            