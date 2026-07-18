class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        left = 0
        seen = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
        '''
        left = 0
        seen = {}
        max_length = 0
        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]] + 1, left)

                
            seen[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length