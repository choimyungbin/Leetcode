# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li = []
        curNode = head
        cntLeft = 1
        cntRight = left+1
        if left == right:
            return head
        # find left
        while curNode and cntLeft != left:
            curNode = curNode.next
            cntLeft+=1
        if curNode and cntLeft == left:   
            li.append(curNode.val)
            curNode = curNode.next
        # find right
        while curNode and cntRight != right:
            li.append(curNode.val)
            curNode = curNode.next
            cntRight += 1
        if curNode and cntRight == right and left != right:
            li.append(curNode.val)
            curNode = curNode.next
        # change values
        curNode = head
        rightIdx = len(li)-1
        cntLeft, cntRight = 1,1
        # go to leftmost val
        while cntLeft != left:
            curNode = curNode.next
            cntLeft += 1
        while rightIdx >= 0:
            curNode.val = li[rightIdx]
            rightIdx-=1
            curNode = curNode.next
            
        return head
            