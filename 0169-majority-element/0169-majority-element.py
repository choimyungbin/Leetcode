class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        threshold = len(nums)//2
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
            if hashMap[n] > threshold:
                return n