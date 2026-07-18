class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        res = nums[0]
        currmin = 1
        currmax = 1
        for num in nums:
            temp = num * currmax

            currmax = max(num * currmax,num * currmin, num)
            currmin = min(temp,num * currmin, num)
            res = max(res, currmax)
        return res