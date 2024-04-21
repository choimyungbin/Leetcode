class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        order = [[] for _ in range((len(nums)+1))]
        res = []
        for n, count in counter.items():
            order[count].append(n)
            
        for i in range(len(order)-1,-1,-1):
            for n in order[i]:
                k -= 1
                res.append(n)
                if k == 0:
                    return res
                