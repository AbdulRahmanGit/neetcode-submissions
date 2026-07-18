class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        #cycle detection
        adj = {i : [] for i in range(num)}
        for crs,pre in pre:
            adj[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if adj[crs] == []:
                return True
            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True
        for c in range(num):
            if not dfs(c):
                return False
        return True