class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr, total):
            if total == 0:
                res.append(list(curr))
                return 
            elif total < 0:
                return
            else:
                '''
                for index in range(i, len(candidates)):
                    if index > i and candidates[i] == candidates[i - 1]:
                        continue
                
                    if total <  candidates[i]:
                        break
                    curr.append(candidates[i])
                    backtrack(i + 1, curr, total - candidates[i])
                    curr.pop()
                '''
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