class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_case(nums[1:]), self.rob_case(nums[:-1]))

    def rob_case(self, nums):
        rob1, rob2 = 0,0
        for i in range(len(nums)):
            newRob = max(nums[i]+rob1, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

            