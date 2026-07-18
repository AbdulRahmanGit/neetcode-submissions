class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = []
        mini = nums[0]
        for i,t in enumerate(nums):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd    
            stack.append((t,i))
        return res

