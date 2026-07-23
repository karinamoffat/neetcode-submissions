class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        results = []

        for i, equation in enumerate(equations):
            adj[equation[0]].append([equation[1], values[i]])
            adj[equation[1]].append([equation[0], 1/values[i]])

        # bfs is only called when we know we need to traverse the graph to get to the equations in terms of
        # the commmon variable
        def bfs(source, pred):
            queue = deque([(source, 1)])
            visited = set()

            while queue:
                curr, weight = queue.popleft()
                if curr == pred:
                    return float(weight)
                
                visited.add(curr)
                for neighbor in adj[curr]:
                    if neighbor[0] not in visited:
                        queue.append([neighbor[0], neighbor[1] * weight])

            return float(-1)

        for query in queries:
            if query[0] not in adj or query[1] not in adj:
                results.append(float(-1))
                continue
            
            results.append(bfs(query[0], query[1]))

        return results