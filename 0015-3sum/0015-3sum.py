class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # for efficiency
            if nums[i] > 0:
                break
            # ⭐️⭐️⭐️⭐️
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # ⭐️⭐️⭐️
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        
        return res