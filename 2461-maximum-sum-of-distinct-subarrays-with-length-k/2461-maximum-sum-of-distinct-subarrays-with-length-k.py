class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        begin = 0
        end = 0
        last = -1
        idxMap = {}
        currSum = 0
        res = 0
        
        while end < len(nums):
            last = idxMap.get(nums[end], -1)
            currSum += nums[end]
            
            while end-begin+1 > k or last >= begin:
                currSum -= nums[begin]
                begin += 1
            if end-begin+1 == k:
                res = max(currSum, res)
            idxMap[nums[end]] = end
            end += 1
            
        return res
            
            
            

                