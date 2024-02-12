class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        majority = len(nums) // 2
        for n in nums:
            hashMap[n] = 1+hashMap.get(n, 0)
            if hashMap[n] > majority:
                return n