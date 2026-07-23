class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        0. define visited and cycles set
        1. for each node in  
        '''
        adj = defaultdict(list)
        for edge in edges:
            if edge[0] == edge[1]:
                return False
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visiting, finished = set(), set()

        def dfs(source):
            if source is None or source in visiting:
                return True
            if source in finished:
                return False
            
            visiting.add(source)
            
            for neighbor in adj[source]:
                if not dfs(neighbor):
                    return False

            visiting.remove(source)
            finished.add(source)
            return True
        
        if len(edges) == 0:
            return True

        if dfs(0):
            if len(finished) == n:
                return True
        return False
        
        
        

    