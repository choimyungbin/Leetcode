class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        # ⭐️⭐️⭐️⭐️ (Because idx is going from right to left)
        idx = r
        
        while l <= r:
            m = (l+r)//2
            if nums[m] <= nums[idx]:
                idx = m
                r = m-1
            elif nums[m] > nums[idx]:
                l = m+1
        
        return nums[idx]