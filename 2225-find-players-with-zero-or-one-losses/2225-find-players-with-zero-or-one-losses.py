class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zeroLoss, oneLoss, moreLoss = set(),set(),set()
        
        for m in matches:
            winner, loser = m[0], m[1]
            
            # add winner
            if winner not in oneLoss and winner not in moreLoss:
                zeroLoss.add(winner)
            
            # add loser
            if loser in zeroLoss:
                zeroLoss.remove(loser)
                oneLoss.add(loser)
            elif loser in oneLoss:
                oneLoss.remove(loser)
                moreLoss.add(loser)
            elif loser in moreLoss:
                continue
            else:
                oneLoss.add(loser)
            
        return [sorted(list(zeroLoss)), sorted(list(oneLoss))]