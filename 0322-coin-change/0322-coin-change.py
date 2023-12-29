class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = {0:0}
        for c in coins:
            dp[c] = 1
        def dfs(amount):
            li = []
            if amount in dp:
                return dp[amount]
            if amount < coins[-1]:
                return -1
            for c in coins:
                if (amount-c)>0:
                    subset = dfs(amount-c)
                    dp[amount-c] = subset
                    if subset == -1:
                        continue
                    li.append(1+subset)
            if not li:
                return -1
            return min(li)
        
        return dfs(amount)