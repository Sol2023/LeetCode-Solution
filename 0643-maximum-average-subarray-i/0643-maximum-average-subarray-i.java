class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
        int maxSum=0;
        int tempSum=0;
        
        for(int i=0; i<k; i++) {
            tempSum+=nums[i];
        }
        
        maxSum = tempSum;
        
        for(int j=k; j<nums.length;j++) {
            
            tempSum = tempSum-nums[j-k]+nums[j];
            
            maxSum = Math.max(maxSum, tempSum);
        }
        
        return maxSum/1.0/k;
        
    }
}