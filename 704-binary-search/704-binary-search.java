class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        
        while(left<=right) {
            int middle = left+(right-left)/2;
            int potential = nums[middle];
            if(potential==target) return middle;
            else if(potential > target){right = middle-1;}
            else left = middle+1;
        }
        return -1;
    }
}