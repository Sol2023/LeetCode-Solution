class Solution {
    public boolean isSubsequence(String s, String t) {
        
        int pivot = 0;
        
        for(int i=0; i<t.length(); i++ ){
            
            if(pivot == s.length()) {
                return true;
            } else if(s.charAt(pivot)==t.charAt(i)) {
                pivot++;
            }
            
        }
        
        return s.length() ==pivot;
        
    }
}