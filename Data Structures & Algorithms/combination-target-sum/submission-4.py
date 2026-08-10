class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def comb(i, curr,total):
            
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return 
            curr.append(nums[i])
            comb(i,curr, total + nums[i])
            curr.pop()
            comb(i+ 1,curr,total)
        comb(0,[],0)
        return res