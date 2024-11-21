class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        last = nums[0]
        # 1. find starting point
        for i in range(1,len(nums)):
            if nums[i] == last:
                idx = i
                break
            else:
                last = nums[i]
                
        if last == nums[-1] and idx==0: return len(nums)
        
        # 2. put numbers
        for i in range(idx+1, len(nums)):
            if nums[i] != last:
                nums[idx] = nums[i]
                idx += 1
                last = nums[i]
        
        return idx