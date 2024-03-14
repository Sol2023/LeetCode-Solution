class Solution {
    public String mergeAlternately(String word1, String word2) {
        
        int l = Math.max(word1.length(), word2.length());
        
        StringBuilder result = new StringBuilder();
        
        for(int i=0; i< l; i++) {
            
            if(i< word1.length()) {
                result.append(word1.charAt(i));
            }
            if (i< word2.length()) {
                result.append(word2.charAt(i));
            }
        }
        
        return result.toString();
        
    }
}