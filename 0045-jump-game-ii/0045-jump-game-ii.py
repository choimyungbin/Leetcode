class Solution:
    def jump(self, nums: List[int]) -> int:
        leftJump = [1000 for i in range(len(nums)-1)]+[0]
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] != 0:
                leftJump[i] = 1 + min(leftJump[i+1:1+min(len(nums)-1,i+nums[i])])
        
        return leftJump[0]
        