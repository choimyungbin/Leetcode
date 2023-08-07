class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1. fresh, q
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    
        # 2. rotting
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if (row<0 or col<0 or row>=ROWS or col>=COLS or
                    grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh -= 1
            time += 1
            
        # 3. return
        return time if fresh == 0 else -1