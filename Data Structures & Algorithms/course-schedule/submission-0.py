class Solution:
    def canFinish(self, numCourses: int, prer: List[List[int]]) -> bool:
        prevmap = {i: [] for i in range(numCourses)}
        for crs, pre in prer:
            prevmap[crs].append(pre)
        visitset = set()
        def dfs(crs):
            if crs in visitset:
                return False
            if prevmap[crs] == []:
                return True
            visitset.add(crs)
            for pre in prevmap[crs]:
                if not dfs(pre):
                    return False
            visitset.remove(crs)
            prevmap[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
