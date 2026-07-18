class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        #most optimised space optimised # O(m + n) O(n)
        dp = [1] * n
        for i in range(1,m):
            for j in range(1, n):
                dp[j] += dp[j -1]
        return dp[-1]
        # O (m * n) # O(n)
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i + 1,j) + dfs(i, j + 1)
        return dfs(0,0)
        '''
        memo = [[-1] * n for _ in range(m)]
        def dfs(i,j):
            if i == (m - 1) and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = dfs(i + 1,j) + dfs(i, j + 1) 
            return memo[i][j] 
        dfs(0,0)
        return dfs(0,0)