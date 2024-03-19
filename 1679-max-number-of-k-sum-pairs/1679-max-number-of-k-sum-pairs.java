class Solution {
    public int maxOperations(int[] nums, int k) {
        
//         // brute force
//         int count =0;
//         int flag = Integer.MIN_VALUE;
        
//         for(int i=0;i<nums.length-1;i++) {
//             for(int j=i+1; j<nums.length; j++) {
//                 if(nums[i]+nums[j]==k) {
//                     count++;
//                     nums[i]=flag;
//                     nums[j]=flag;
//                 }
                
//             }
//         }
//         return count;
        
        int left =0;
        int right =nums.length-1;
        int count =0;
        
        Arrays.sort(nums);
        
        while(left < right) {
            
            if(nums[left]+nums[right]==k) {
                count++;
                left++;
                right--;
            } else if (nums[left]+nums[right]>k) {
                right--;
            } else left++;
            
        }
        
        return count;
        
    }
}