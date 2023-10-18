class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # bc the biggest num nums can haave is len(nums)
        buck = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1+count.get(n, 0)
        # {1:3, 2:2, 3:1}
        for n, c in count.items():
            buck[c].append(n)
        # [[], [3], [2], [1], [], []]
        for i in range(len(buck)-1, 0, -1):
            for e in buck[i]:
                res.append(e)
                if len(res) == k:
                    return res