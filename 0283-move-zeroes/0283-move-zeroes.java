class Solution {
    public void moveZeroes(int[] nums) {
        
        int point =0;
        
        for(int num: nums){
            
            if(num!=0) {
                nums[point++]=num;
            }
        }
        
        while(point<nums.length) {
            nums[point++]=0;
        }
        
        // return nums;
    }
    
}