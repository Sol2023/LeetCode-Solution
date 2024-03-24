class Solution {
    public int largestAltitude(int[] gain) {
        
        
        int tempHight = 0;
        
        int res = 0;
        
        for(int g: gain) {
            
            tempHight+=g;
            
            res=Math.max(res, tempHight);
        }
        
        return res;
        
        
        
    }
}