class Solution {
    public int longestOnes(int[] nums, int k) {
        
        int left =0, right;
        int numZero=0;
        int max=0;
        
        
        for(right=0; right<nums.length; right++) {
            
            if(nums[right]==0) {
                numZero++;
                // k--;
            }
            
            if(numZero>k) {
                
                if(nums[left]==0) numZero--;
                left++;
                
            }
            
            if(numZero<=k) {
                
                max = Math.max(max, right-left+1);
            }
        }
        
        return max;
        
    }
}