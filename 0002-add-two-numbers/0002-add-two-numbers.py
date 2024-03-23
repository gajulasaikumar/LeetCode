# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def solve(t):
            l=[]
            while t:
                l.append(str(t.val))
                t=t.next
                
            return l
        x=solve(l1)[::-1]
        y=solve(l2)[::-1]
        p=[]
        print(x,y)
        x=int("".join(x))
        y=int("".join(y))
        for i in str(x+y)[::-1]:
            p.append(int(i))
        h=ListNode(p[0])
        m=h
        for i in range(1,len(p)):
            t=ListNode(p[i])
            m.next=t
            m=t
        return h
            
        
        
                
            