class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # root, one parent, all connected, no cycle
        
        def find_root():
            # set with OR: automatic sorting & remove duplicates
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        
        # 1. find root idx
        root = find_root()
        if root == -1:
            return False
        
        # 2. dfs using stack
        seen = {root}   # set
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    # see multiple parents (or cycle, which has multiple parents)
                    if child in seen:
                        return False
                    
                    stack.append(child)
                    seen.add(child)
        return len(seen) == n