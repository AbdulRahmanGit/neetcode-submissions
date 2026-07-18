class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        n = len(nums)
        dp = [1000000] * n
        dp[-1] = 0
        for i in range(n -1, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i+ 1, end):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]
        '''
        res = 0
        l , r = 0, 0
        while r < len(nums) - 1:
            highest_jump = 0
            for i in range(l, r+ 1):
                highest_jump = max(highest_jump,  i + nums[i])
            l = r + 1
            r = highest_jump
            res += 1
        return res