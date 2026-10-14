# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        c = head

        while c is not None:
            nn = c.next # store the next node
            c.next = p # reverse the next node for the current node
            p = c # advance the previous node
            c = nn # advance the current node

        return p
        
