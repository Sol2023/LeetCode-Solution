class Solution {
    public int[] twoSum(int[] nums, int target) {
        
//         for(int i=0; i<nums.length-1; i++) {
//             for(int j=i+1; j<nums.length; j++) {
//                 int candidate = nums[i] + nums[j];
                
//                 if(candidate ==target) {
//                     return new int [] {i, j};
//                 }
//             }
//         }
//         return null;
        
        Map<Integer,Integer> dit = new HashMap<>();
        
        for(int i=0; i< nums.length;i++) {
            
            int candidate = target - nums[i];
            
            if(dit.containsKey(candidate)) {
                return new int [] {dit.get(candidate), i};
            } else {
                dit.put(nums[i], i);
            }
        }
        return null;
        
    }
}