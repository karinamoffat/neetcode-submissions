class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}
        visited = set()

        for src, pred in prerequisites:
            courseMap[src].append(pred)

        def dfs(node):
            if node in visited:
                return False
            
            if courseMap[node] == []:
                return True
            
            visited.add(node)
            for neighbor in courseMap[node]:
                if not dfs(neighbor):
                    return False
            visited.remove(node)
            courseMap[node] = []
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True

