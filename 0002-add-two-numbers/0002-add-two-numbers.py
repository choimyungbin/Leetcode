# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p1, p2 = l1, l2
        ten = 0
        before = dummy
        while p1 or p2 or ten:
            digitSum = (p1.val if p1 else 0)+(p2.val if p2 else 0)+ten
            before.next = ListNode(digitSum % 10)
            ten = digitSum // 10
            before = before.next
            p1 = (p1.next if p1 else p1)
            p2 = (p2.next if p2 else p2)
        
        
        return dummy.next