class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashMap = {}
        nums.sort()
        
        for i, n in enumerate(nums):
            # important!!!
            # if n is not first num but the biggest
            if i>0 and n == nums[i-1]:
                continue
            # important!!
            # set l = i+1
            l, r = i+1, len(nums)-1
            while l < r:
                total = n+nums[l]+nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
                    