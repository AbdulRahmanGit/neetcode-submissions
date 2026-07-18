class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S_map  = {}
        T_map = {} 
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            S_map[s[i]] = 1 + S_map.get(s[i], 0)
            T_map[t[i]] = 1 + T_map.get(t[i], 0)
        return S_map == T_map