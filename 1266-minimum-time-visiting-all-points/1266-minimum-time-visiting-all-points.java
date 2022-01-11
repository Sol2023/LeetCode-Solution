class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        if(points.length<2) return 0;
        
        int stepNum = 0;
        
        for(int i=0; i< points.length-1; i++) {
            stepNum+=Math.max(Math.abs(points[i][0]-points[i+1][0]), Math.abs(points[i][1]-points[i+1][1]));
        }
        
        return stepNum;
        
    }
}