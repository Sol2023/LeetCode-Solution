class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int maxArea = 0;
        for(int i =0; i<m; i++){
            for(int j =0; j<n;j++){
                if(grid[i][j]==1){
                    maxArea = Math.max(maxArea, explore(grid,i,j));
                }
                
            }
            
        }
        return maxArea;
    }
    
    public int explore(int[][] grid, int i, int j){
        if(i>=0 && i<grid.length && j>=0 && j<grid[0].length && grid[i][j]==1){
            grid[i][j]=0;
            return 1+ explore(grid, i-1,j)+explore(grid,i+1,j)+explore(grid,i,j-1)+explore(grid,i,j+1);
            
        }
        return 0;
    }
}