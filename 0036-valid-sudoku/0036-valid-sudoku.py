class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9
        # 1. check rows
        for row in board:
            nums = set()
            for n in row:
                if n == ".":
                    continue
                if n in nums:
                    return False
                nums.add(n)
        
        # 2. check columns
        colNums = [set() for _ in range(COLS)]
        for row in board:
            for i,n in enumerate(row):
                if n == ".":
                    continue
                if n in colNums[i]:
                    return False
                colNums[i].add(n)
        
        # 3. check squares
        squares = [[set(),set(),set()] for _ in range(ROWS//3)]
        for i in range(len(board)):
            for j,n in enumerate(board[i]):
                if n == ".":
                    continue
                if n in squares[i//3][j//3]:
                    return False
                squares[i//3][j//3].add(n)
        
        return True