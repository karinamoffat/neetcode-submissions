class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        island is a graph, multiple islands is a series of disjoin graphs
        we need to count how many elements each disjoin graph has

        return: int = maximum area

        pseudocode:
        1) find the first one
        2) if this node with the 1 is in visited, return max_area
        3) check if adjacent nodes are a 1. grid[0][i+1] or grid[0-1] or grid[]
        '''
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, grid, visited):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            return (1+ dfs(r, c-1, grid, visited) + dfs(r, c+1, grid, visited) + dfs(r-1, c, grid, visited) + dfs(r+1, c, grid, visited))

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    area = dfs(r, c, grid, visited)
                    visited.add((r, c))
                    if area > max_area:
                        max_area = area
        
        return max_area


            
