class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIdx = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[insertIdx] = nums[i]
                insertIdx += 1
        return insertIdx