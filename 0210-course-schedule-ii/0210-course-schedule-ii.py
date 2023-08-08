class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        preMap = { i:[] for i in range(numCourses) }
        cycle, visit = set(), set()
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            output.append(course)
            visit.add(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return output