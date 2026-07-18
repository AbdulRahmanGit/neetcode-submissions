class Solution:
    def rob(self, nums: List[int]) -> int:
        res1, res2 = 0, 0
        for n in nums:
            temp = max(n + res1, res2)
            res1 = res2
            res2 = temp
        return res2