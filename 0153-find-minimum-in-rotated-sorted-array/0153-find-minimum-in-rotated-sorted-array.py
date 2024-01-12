class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 2,1
        
        l, r = 0, len(nums)-1
        smallest = nums[0]
        while l <= r:
            m = (l+r)//2
            # left is sorted
            if nums[l] <= nums[m]:
                smallest = min(smallest, nums[l])
                l = m+1
            # right is sorted
            else:
                smallest = min(smallest, nums[m])
                r = m-1
        
        return smallest