class Solution {
    public int maxArea(int[] height) {
        int ans = 0, left=0, right=height.length-1;
        while(left<right){
            if(height[left]<height[right]){
                ans = Math.max(ans, (right-left)*Math.min(height[left],height[right]));
                left++;
            }
            else { ans = Math.max(ans, (right-left)*Math.min(height[left],height[right]));
                right--;}
        }
        return ans;
    }
        
}