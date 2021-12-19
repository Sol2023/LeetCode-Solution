class Solution {
    public int removeDuplicates(int[] nums) {
        int left=0;
        for(int num : nums){
            if(left<2 || num!=nums[left-2]){
                nums[left++]=num;
            }   
        }
        return left;
    }
}