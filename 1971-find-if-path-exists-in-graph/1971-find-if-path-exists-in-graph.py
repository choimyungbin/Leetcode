class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)    
        visit = set()
        
        for start, end in edges:
            neighbors[start].append(end)
            neighbors[end].append(start)
        
        def dfs(cur):
            if cur == destination:
                return True
            
            visit.add(cur)
            for nei in neighbors[cur]:
                if nei not in visit:
                    res = dfs(nei)
                    if res: return True
                
            return False
        
        return dfs(source)