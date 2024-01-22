class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 1. get duplicate
        numSet = set()
        duplicate = 0
        missing = 0
        for n in range(1,len(nums)+1):
            if n not in nums:
                missing = n
        for n in nums:
            # not duplicate
            if n not in numSet:
                numSet.add(n)
            # duplicate
            else:
                duplicate = n
        
        return [duplicate, missing]