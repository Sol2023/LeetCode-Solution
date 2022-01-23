class Solution {
    public int thirdMax(int[] nums) {
        Integer Max1=null;
        Integer Max2=null;
        Integer Max3=null;
        
        for(Integer n:nums){
            if(n.equals(Max1) || n.equals(Max2) || n.equals(Max3)) continue;
            if(Max1==null || n>Max1){
                Max3=Max2;
                Max2=Max1;
                Max1=n;
            } else if(Max2==null || n>Max2){
                Max3=Max2;
                Max2=n;
            } else if(Max3==null || n>Max3){
                Max3=n;
            }
        }
        
        return Max3==null? Max1:Max3;
        
    }
}