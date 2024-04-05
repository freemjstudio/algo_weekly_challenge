from types import List 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0

        def dfs(grid, i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != '1':
                return 
            
            grid[i][j] = '0'

            dfs(grid, i-1 , j)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count

        

