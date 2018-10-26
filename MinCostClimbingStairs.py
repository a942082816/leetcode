class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 2:
            return min(cost)
        dp = [0] * len(cost)
        for i, v in enumerate(cost):
            if i == 0:
                dp[0] = cost[0]
            if i == 1:
                dp[1] = cost[1]
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + v
        return min(dp[-1], dp[-2])



S = Solution()
print(S.minCostClimbingStairs([0,1,1,0]))


