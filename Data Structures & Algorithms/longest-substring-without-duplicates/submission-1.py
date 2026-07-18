class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        for i in range(len(s)):
            seen = set()
            for right in range(i,len(s)):
                if s[right] in seen:
                    break


                seen.add(s[right])
            max_length = max(max_length, len(seen))
        return max_length
