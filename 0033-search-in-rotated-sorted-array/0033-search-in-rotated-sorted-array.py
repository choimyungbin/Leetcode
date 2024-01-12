class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        idx = -1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                idx = m
                break
            
            # left is sorted
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m+1
                else:
                    r = m-1
            # right is sorted
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1
            
        return idx