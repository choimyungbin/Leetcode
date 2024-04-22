class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        q.append(["0000",0])
        visit = set(deadends)
        if "0000" in visit:
            return -1
        def children(parent):
            res = []
            for i in range(len(parent)):
                digit = str((int(parent[i]) + 1)%10)
                res.append(parent[:i]+digit+parent[i+1:])
                digit = str((int(parent[i]) - 1 + 10)%10)
                res.append(parent[:i]+digit+parent[i+1:])
            return res
        
        while q:
            cur, turn = q.popleft()
            if cur == target:
                return turn
            for child in children(cur):
                if child not in visit:
                    q.append([child, turn+1])
                    visit.add(child)
                    
        return -1