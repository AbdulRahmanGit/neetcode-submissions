class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]


        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self,nums):
        '''
        first = 0
        second = 0
        for num in nums:
            newrob = max(first + num, second)
            first = second
            second = newrob
        return second
        '''
        
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]
        