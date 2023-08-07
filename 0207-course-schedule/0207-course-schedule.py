class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        
        # define preMap
        preMap = { i:[] for i in range(numCourses) }
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # define dfs func
        def dfs(course):
            # cycle
            if course in visit:
                return False
            # no pre
            if preMap[course] == []:
                return True
            
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visit.remove(course)
            preMap[course] = []
            return True
            
        # iterate
        for course in range(numCourses):
            if not dfs(course): return False
        return True