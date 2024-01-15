class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        scores = {}
        res = [[],[]]
        # make scoreboard
        for m in matches:
            if m[0] not in scores.keys():
                scores[m[0]] = [0,0]
            if m[1] not in scores.keys():
                scores[m[1]] = [0,0]
            scores[m[0]][0] += 1
            scores[m[1]][1] += 1
        
        for player in scores.keys():
            if scores[player][1] == 0:
                res[0].append(player)
            elif scores[player][1] == 1:
                res[1].append(player)
        res[0].sort()
        res[1].sort()
        return res