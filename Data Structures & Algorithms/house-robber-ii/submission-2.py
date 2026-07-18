class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self,nums):
        first = 0
        second = 0
        for num in nums:
            newrob = max(first + num, second)
            first = second
            second = newrob
        return second