class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        cache = [0]*len(nums)
        def dfs(i):
            # base case:
            if cache[i]:
                return cache[i]
            if i == len(nums)-1 or nums[i] >= max(nums[i+1:]):
                cache[i] = 1
                return 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1+dfs(j))
            return cache[i]
                
        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res