"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodesMap = {}
        curr = head
        if not head:
            return None
        # 1. make nodes & connect with original linked list
        while curr:
            nodesMap[curr] = Node(curr.val)
            curr = curr.next
        
        # 2. set next, random
        curr = head
        while curr:
            nodesMap[curr].next = nodesMap.get(curr.next, None)
            nodesMap[curr].random = nodesMap.get(curr.random, None)
            curr = curr.next
            
        return nodesMap[head]