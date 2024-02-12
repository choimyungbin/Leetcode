class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for n, count in counter.items():
            if count > len(nums)//2:
                return n