class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        c = collections.Counter()
        for x, t in groupby(colors):
            # If 3 letters are consecutive, 1 is recognized, so -2
            c[x] += max(len(list(t)) - 2, 0)

        if c['A'] > c['B']:
            return True
        return False