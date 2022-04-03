class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def explore(r, c):
            if  0<=r<m and 0<=c<n and grid[r][c]:
                grid[r][c]=0
                return 1+explore(r-1,c)+explore(r+1,c)+explore(r,c-1)+explore(r,c+1)
            return 0
        
        areas = [explore(i,j) for i in range(m) for j in range(n) if grid[i][j]]
        
        return max(areas) if areas else 0
            
        