class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        countList = [[] for _ in range(len(nums)+1)]
        order = 0
        res = []
        
        for n in counter.keys():
            countList[counter[n]].append(n)
        for i in range(len(nums),-1,-1):
            for n in countList[i]:
                if order < k:
                    res.append(n)
                    order += 1
        
        return res
                
        