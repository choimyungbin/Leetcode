class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                hashSet.remove(num)
            else:
                hashSet.add(num)
                
        return hashSet.pop()