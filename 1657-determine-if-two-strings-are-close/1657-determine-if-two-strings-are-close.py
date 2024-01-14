class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        map1, map2 = {}, {}
        set1, set2 = set(),set()
        map1 = Counter(word1)
        map2 = Counter(word2)
        for k in map1.keys():
            set1.add(k)
        for k in map2.keys():
            set2.add(k)
        if set1 != set2 or sorted(map1.values()) != sorted(map2.values()):
            return False
        return True