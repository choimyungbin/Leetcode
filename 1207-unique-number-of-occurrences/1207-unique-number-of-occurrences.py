class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        numSet = set()
        for n in counter.values():
            if n in numSet:
                return False
            numSet.add(n)
        return True