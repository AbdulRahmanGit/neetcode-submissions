class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        freq = {}
        res = 0
        for right in range(len(s)):
            
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_len = max(max_len, freq[s[right]])
            
            while (right - left + 1) - max_len > k:
                
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res

