class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        res1, res2 = 0, 0
        for n in nums:
            temp = max(n + res1, res2)
            res1 = res2
            res2 = temp
        return res2
    '''
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0 
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        return dfs(0)