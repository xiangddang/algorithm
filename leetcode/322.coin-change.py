#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if i >= j and dp[i - j] != -1:
                    if dp[i] == -1 or dp[i] > dp[i - j] + 1:
                        dp[i] = dp[i - j] + 1
        return dp[amount]
# @lc code=end

