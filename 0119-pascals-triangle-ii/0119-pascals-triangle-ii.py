class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fact(n):
            if n <= 1:
                return 1
            else:
                return n*fact(n-1)
        
        res = []
        for i in range(rowIndex+1):
            res.append(fact(rowIndex)//(fact(rowIndex-i)*fact(i)))
            
        return res