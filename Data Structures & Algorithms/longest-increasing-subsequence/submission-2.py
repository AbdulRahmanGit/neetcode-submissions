
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp = []
        dp.append(nums[0])
        lis = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                lis += 1
                continue
            idx = bisect_left(dp,nums[i])
            dp[idx] = nums[i]
        return lis
        '''
        n = len(nums)
        dp = [1] * len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
