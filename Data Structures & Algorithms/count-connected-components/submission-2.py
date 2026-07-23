class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        we do a dfs
        once dfs ends for that iteration, increment components counter
            if len(finished) == n: return counter
            search the finished set for the next starting node

        '''
        adj = defaultdict(list)
        # visiting is used within dfs to track cycles
        # finished is used to find the next starting node for the next component
        visiting, finished = set(), set()
        components = 0

        for edge in edges:
            if edge[0] == edge[1]:
                continue
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(source):
            if source is None or source in visiting or source in finished:
                return

            visiting.add(source)

            for neighbor in adj[source]:
                dfs(neighbor)
            
            visiting.remove(source)
            finished.add(source)
            return
            

        for node in range(n):
            if len(finished) == n:
                return components
            if node in finished:
                continue
            dfs(node)
            components += 1
        
        return components
        




    