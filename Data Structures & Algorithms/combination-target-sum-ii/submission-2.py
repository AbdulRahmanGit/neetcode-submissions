class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        res = []
        def backtrack(i, curr, total):
            if total == 0:
                res.append(list(curr))
                return 
            elif total < 0:
                return
            else:
                
                for index in range(i, len(candidates)):
                    if index > i and candidates[i] == candidates[i - 1]:
                        continue
                
                    if total <  candidates[i]:
                        break
                    curr.append(candidates[i])
                    backtrack(i + 1, curr, total - candidates[i])
                    curr.pop()
                for index in range(i, len(candidates)):
                    if index > i and candidates[index] == candidates[index-1]:
                        continue
                    if total < candidates[index]:
                        break

                    curr.append(candidates[index])
                    backtrack(index + 1, curr,total - candidates[index])
            
                    curr.pop()
        candidates.sort()
        backtrack(0,[], target)
        return res
        '''
        res = []
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if len(nums) == i or total > target:
                return
            curr.append(nums[i])
            backtrack(i + 1,curr, total + nums[i])
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr, total)


        nums.sort()
        backtrack(0,[],0)
        return res

