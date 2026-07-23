class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        minutes = 0
        queue = deque()

        def addCell(r, c, grid):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited:
                return
            
            visited.add((r, c))

            if grid[r][c] == 0:
                return
            
            queue.append((r, c))
            return


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))

        if len(queue) == 0:
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        return -1
            else:
                return minutes

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                addCell(r - 1, c, grid)
                addCell(r + 1, c, grid)
                addCell(r, c - 1, grid)
                addCell(r, c + 1, grid)

                if grid[r][c] == 1:
                    grid[r][c] = 2
                
                if len(queue) == 0:
                    if len(visited) == ROWS * COLS:
                        return minutes
        
                    else:
                        return -1
            
            minutes += 1
