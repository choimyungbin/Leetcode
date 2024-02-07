class Solution:
    def frequencySort(self, s: str) -> str:
        c1, c2 = Counter(s), {}
        for k,v in c1.items():
            if v not in c2:
                c2[v] = []
            c2[v].append(k*v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])