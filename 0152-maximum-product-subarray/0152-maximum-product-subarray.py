class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # get the minimum value ⭐️⭐️⭐️⭐️
        curMin, curMax = 1,1
        res = max(nums)
        for n in nums:
            temp = curMin # ⭐️
            curMin = min(n, curMin*n, curMax*n)
            curMax = max(n, temp*n, curMax*n)
            res = max(res, curMax)
        return res