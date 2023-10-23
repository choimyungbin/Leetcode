class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPos = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goalPos:
                goalPos = i
                
        return goalPos == 0