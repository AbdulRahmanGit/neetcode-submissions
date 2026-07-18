class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        res = 0
        store = set(nums)
        for i in nums:
            streak, curr = 0, i
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return 
        '''
        mp = defaultdict(int)
        res = 0
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res,mp[num])
        return res

        