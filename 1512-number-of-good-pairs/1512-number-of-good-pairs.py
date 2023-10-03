class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = defaultdict(list)
        res = 0
        
        for i, n in enumerate(nums):
            hashMap[n].append(i)
        
        for n in hashMap.keys():
            res += int(self.fact(len(hashMap[n]))/(2*self.fact(len(hashMap[n])-2))) 
        
        return res
        
    def fact(self, n):
        if n <= 1:
            return 1
        return n*(self.fact(n-1))
        
        