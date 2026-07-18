class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = strs[0]
        # for i in range(len(strs)):
        #     j = 0
        #     while j < min(len(strs[i]), len(prefix)):
        #         if strs[i][j] != prefix[j]:
        #             break
        #         j += 1

        #     prefix = prefix[:j]
        # return prefix
        res = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res