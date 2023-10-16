class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        prev = 1
        for k in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - k + 1) // k
            res.append(next_val)
            prev = next_val
        return res
    # 4C0 4C1 4C2 4C3 4C4
    # 1    4    6  4   1
    # 4!/0!4!
    # 4!/1!3!
    # 4!/2!2!