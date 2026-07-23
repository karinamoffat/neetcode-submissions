class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        results = []
        queue = deque()

        for src, pred in prerequisites:
            inDegree[pred] += 1
            adj[src].append(pred)

        for node in range(numCourses):
            if inDegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            results.append(node)
            for neighbor in adj[node]:
                inDegree[neighbor] -=1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
            
        if len(results) == numCourses:
            return results[::-1]
        else:
            return []
        
