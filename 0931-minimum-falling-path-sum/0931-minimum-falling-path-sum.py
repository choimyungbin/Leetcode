class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        
        for r in range(1,N):
            for c in range(N):
                left = matrix[r-1][c-1] if c-1 >= 0 else float("inf")
                mid = matrix[r-1][c]
                right = matrix[r-1][c+1] if c+1 < N else float("inf")
                matrix[r][c] = matrix[r][c] + min(left, mid,right)
        
        return min(matrix[-1])