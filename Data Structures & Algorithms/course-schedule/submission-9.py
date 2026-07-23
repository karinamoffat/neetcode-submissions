class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        queue = deque()

        for src, pred in prerequisites:
            inDegree[pred] += 1
            adj[src].append(pred)

        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)

        finished = 0
        while queue:
            finished += 1
            curr = queue.popleft()

            for neighbor in adj[curr]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        if finished == numCourses:
            return True
        else:
            return False
