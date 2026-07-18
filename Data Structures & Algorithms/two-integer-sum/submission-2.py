class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            prev[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev and prev[diff] != i:
                return [i, prev[diff]] 
            

