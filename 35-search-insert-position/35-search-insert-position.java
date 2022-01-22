class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        
        while(left<=right){
            int middle = left+ (right-left)/2;
            int potential = nums[middle];
            if(target == potential){
                return middle;
            } else if(target < potential){
                right = middle-1;
            } else left=middle+1;
        }
        
        return left;
        
    }
}