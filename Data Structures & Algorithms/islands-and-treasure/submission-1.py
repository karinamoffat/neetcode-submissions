class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()

        visited = set()

        def addCell(r, c, grid, distance):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            queue.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
                
        distance = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance

                addCell(r-1, c, grid, distance)
                addCell(r+1, c, grid, distance)
                addCell(r, c-1, grid, distance)
                addCell(r, c+1, grid, distance)

            distance += 1

