class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = nums[0]
        for num in nums:
            if currsum < 0:
                currsum = 0
            currsum += num
            maxsum = max(maxsum, currsum)
        return maxsum

