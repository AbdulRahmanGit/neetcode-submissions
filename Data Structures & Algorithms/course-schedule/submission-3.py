class Solution:
    def canFinish(self, numcourse: int, pre: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numcourse)}
        visited = set()
        #as directed graph appending course(src) and pre (dst)
        for crs, pre in pre:
            adj[crs].append(pre)
        def dfs(crs):
            # it means cycle not detected
            if crs  in visited:
                return False
            # means cycle detected 
            if adj[crs] == []:
                return True
            visited.add(crs)
            for prev in adj[crs]:
                if not dfs(prev):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True
        for c in range(numcourse):
            if not dfs(c):
                return False
        return True
