class Solution {
    public int findMin(int[] nums) {
        
        // 5 6 1 2 3 4; l=6 
        
        
        if(nums.length==1) return nums[0];
        
        if(nums[0]<nums[nums.length-1]) return nums[0];
        
        int left=0;
        int right=nums.length-1;
        
        
        while(left<right) {
            int mid = left+ (right-left)/2;
            
            if(mid-1>=0 && nums[mid]<nums[mid-1]) return nums[mid];
            
            if(mid+1<= nums.length && nums[mid]>nums[mid+1]) return nums[mid+1];
            
            if(nums[mid]<nums[0]) right =mid-1;
            else left = mid+1;
            
            
        }
        return -1;
        
      
    }
}