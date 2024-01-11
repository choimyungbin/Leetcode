class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hashSet = set(nums)
        if target not in hashSet:
            return -1
        return bisect_left(nums, target)