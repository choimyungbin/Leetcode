class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            if target-n in hashMap:
                return [i, hashMap[target-n]]
            
            hashMap[n] = i