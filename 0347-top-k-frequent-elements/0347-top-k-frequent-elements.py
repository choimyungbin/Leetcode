class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # use freq as idx
        buck = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1+count.get(n,0)
        for n,c in count.items():
            buck[c].append(n)
        # [[], [3], [2], [1], [], []]
        res = []
        # iterate backward to get most frequent numbers first
        for i in range(len(buck)-1,0,-1):
            for e in buck[i]:
                res.append(e)
                if len(res)==k:
                    return res