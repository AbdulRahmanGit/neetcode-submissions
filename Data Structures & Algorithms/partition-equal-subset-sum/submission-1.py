class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        total = sum(nums)//2
        memo = [[-1] * (total + 1) for i in range(len(nums) + 1)]
        def dfs(i, target):
            if i >= len(nums) or target < 0 :
                return target == 0
            if target == 0:
                return True
            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[i][target]
        return dfs(0,total)