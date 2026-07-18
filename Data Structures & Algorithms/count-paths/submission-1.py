class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        #most optimised space optimised
        dp = [1] * n
        for i in range(1,m):
            for j in range(1, n):
                dp[j] += dp[j -1]
        return dp[-1]
        '''
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i + 1,j) + dfs(i, j + 1)
        return dfs(0,0)