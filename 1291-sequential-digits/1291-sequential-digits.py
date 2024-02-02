class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = [[] for _ in range(len(str(high))-len(str(low))+1)]
        digits = "123456789"
        lowLen = len(str(low))
        for l in range(10-lowLen):
            r = l+lowLen
            idx = 0
            while r <= len(digits):
                num = int(digits[l:r])
                if num > high:
                    break
                elif num >= low:
                    res[idx].append(num)
                r += 1
                idx += 1
        
        return [item for sublist in res for item in sublist]