class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1: nums[i-2], rob2: nums[i-1]
        rob1, rob2 = 0, 0
        
        for n in nums:
            res = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = res
            
        return res
        
        