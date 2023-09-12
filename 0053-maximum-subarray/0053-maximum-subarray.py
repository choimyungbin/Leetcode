class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        rPtr = 0
        
        for n in nums:
            if rPtr < 0:
                rPtr = 0
            rPtr += n
            res = max(res, rPtr)
        return res