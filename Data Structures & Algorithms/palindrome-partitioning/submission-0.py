class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) <= 1:
            return [[s]]
        temp_list = []
        res = []
        def backtrack(j,i, temp_list):
            if i >= len(s):
                if i == j:
                    res.append(temp_list.copy())
                return 
            if self.ispalin(s,j,i):
                temp_list.append(s[j:i + 1])
                backtrack(i+ 1 , i + 1, temp_list)
                temp_list.pop()
            backtrack(j,i+ 1, temp_list)
        


        backtrack(0,0,[])
        return res
    def ispalin(self,s,l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            l,r = l + 1, r - 1
        return True


        