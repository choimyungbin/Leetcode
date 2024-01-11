class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        pastTemps = []
        
        for i, cTemp in enumerate(temperatures):
            while pastTemps and pastTemps[-1][0] < cTemp:
                pTemp = pastTemps.pop()
                res[pTemp[1]] = i - pTemp[1]
                    
            pastTemps.append([cTemp, i])
        
        return res