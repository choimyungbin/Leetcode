# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        
        while node.next:
            if not node.next.next:
                break
            tail = node
            temp = node.next
            while tail.next.next:
                tail = tail.next
            node.next = tail.next
            if node != tail:
                tail.next = None
            node.next.next = temp
            node = temp
        
        return head