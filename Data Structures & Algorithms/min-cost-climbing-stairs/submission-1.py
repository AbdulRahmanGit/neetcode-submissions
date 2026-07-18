class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ''''
        memo = [-1] * len(cost)
        def helper(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(helper(i + 1), helper(i + 2))
            return memo[i]
        return min(helper(0),helper(1))
        '''
        for i in range(len(cost) - 3, - 1, -1):
            cost[i] += min(cost[i+ 1], cost[i+2])
        return min(cost[0], cost[1])