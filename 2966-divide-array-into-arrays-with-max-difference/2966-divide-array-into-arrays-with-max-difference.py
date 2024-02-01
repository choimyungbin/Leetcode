class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        greedy = [0]* len(nums)
        res = [[nums[0]]]
        t = 1
        for i in range(1,len(nums)):
            if t == 0:
                res.append([nums[i]])
            elif nums[i] - res[-1][0] <= k:
                res[-1].append(nums[i])
            else:
                return []
            t = (t+1)%3
        
        return res