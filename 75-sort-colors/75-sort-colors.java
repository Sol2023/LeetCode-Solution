class Solution {
    public void sortColors(int[] nums) {
        boolean isSorted=false;
        int count=0;
        
        while(!isSorted){
            isSorted=true;
            
            for(int i=0; i<nums.length-1-count;i++){
                if(nums[i]>nums[i+1]){
                    swap(i,i+1, nums);
                }
                isSorted=false;
            }
            count++;
        }
        
    }
    
    public static void swap(int nums1, int nums2, int[] array){
        int temp = array[nums1];
        array[nums1]= array[nums2];
        array[nums2]= temp;
    }
}