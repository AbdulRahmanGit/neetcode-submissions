class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        r = 0
        length = 0
        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)
            while len(s[l:r + 1]) - max(seen.values())> k:
                seen[s[l]] -= 1
                l += 1
                
                
            
            length = max(length, r - l + 1)
        return length
                

        

