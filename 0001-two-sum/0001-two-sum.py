class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {num:idx}
        hashMap = {}
        for i, n in enumerate(nums):
            if target-n in hashMap.keys():
                return [i, hashMap[target-n]]
            hashMap[n] = i