class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)    
        visit = set()
        queue = deque()
        
        for start, end in edges:
            neighbors[start].append(end)
            neighbors[end].append(start)
        
        queue.append(source)
        
        while queue:
            cur = queue.popleft()
            visit.add(cur)
            if cur == destination:
                return True
            for nei in neighbors[cur]:
                if nei not in visit:
                    queue.append(nei)
                    
        return False