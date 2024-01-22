class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numSet = set()
        duplicate = 0
        missing = 0
        for n in nums:
            if n not in numSet:
                numSet.add(n)
            else:
                duplicate = n
        for n in range(1,len(nums)+1):
            if n not in numSet:
                missing = n
        
        return [duplicate, missing]