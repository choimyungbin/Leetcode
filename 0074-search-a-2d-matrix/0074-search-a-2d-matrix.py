class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1
        
        # find the row
        while top <= bot:
            mid = (top+bot)//2
            if target < matrix[mid][0]:
                bot = mid-1
            elif target > matrix[mid][-1]:
                top = mid+1
            else:
                row = mid
                break
                
        if top > bot:
            return False
        
        l, r = 0, COLS-1
        # find the column
        while l <= r:
            m = (l+r)//2
            if target < matrix[row][m]:
                r = m-1
            elif target > matrix[row][m]:
                l = m+1
            else:
                return True
        return False