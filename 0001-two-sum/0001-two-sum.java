class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        for(int i=0; i<nums.length-1; i++) {
            for(int j=i+1; j<nums.length; j++) {
                int candidate = nums[i] + nums[j];
                
                if(candidate ==target) {
                    return new int [] {i, j};
                }
            }
        }
        return null;
        
    }
}