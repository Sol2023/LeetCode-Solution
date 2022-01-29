class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean isNonIncreasing = true;
        boolean isNonDecreasing = true;
        
        for(int i=1; i<nums.length; i++) {
            int difference = nums[i]-nums[i-1];
            
            if(difference >0) isNonIncreasing = false;
            if(difference <0) isNonDecreasing = false;
            
        }
        
        return isNonIncreasing || isNonDecreasing;
            
        
        
    }
}