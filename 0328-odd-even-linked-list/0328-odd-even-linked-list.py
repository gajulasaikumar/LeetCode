# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        t=head
        l=[]
        while t!=None and t.next!=None:
            l.append(t.val)
            t=t.next.next
        if t:
            l.append(t.val)
        t=head.next
        while t!=None and t.next!=None:
            l.append(t.val)
            t=t.next.next
        if t:
            l.append(t.val)
        x=head
        i=0
        while x:
            x.val=l[i]
            i+=1
            x=x.next
        return head
        
        
            
            