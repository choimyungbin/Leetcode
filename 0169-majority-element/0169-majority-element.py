class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = 0
        for n in nums:
            if count == 0 and n != cand:
                cand = n
            if n == cand:
                count += 1
            else:
                count -= 1
        return cand