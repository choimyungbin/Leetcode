class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        res = -1
        while l < r:
            if target > nums[(l+r)//2]:
                l = (l+r)//2 + 1
            elif target < nums[(l+r)//2]:
                r = (l+r)//2 - 1
            else:
                res = (l+r)//2
                break
        if l == r and nums[l] == target:
            res = l
        return res