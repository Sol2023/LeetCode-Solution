class Solution {
    public String reverseWords(String s) {
        
        String[] words = s.split("\\s+");
        
        int left = 0;
        int right = words.length-1;
        
        while(left < right) {
            String temp = words[left];
            words[left] = words[right];
            words[right] = temp;
            left++;
            right--;
        }
        
        return String.join(" ", words).trim();
        
    }
}