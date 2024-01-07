class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        
        # hashMaps[i][diff] = # of sub with diff ending at i
        hashMaps = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                hashMaps[i][diff] += 1 + hashMaps[j][diff]
                res += 1 + hashMaps[j][diff]
        
        return res - (n * (n-1) // 2)