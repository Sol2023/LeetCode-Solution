class Solution {
    public String reverseVowels(String s) {
        
        char[] vowels = {'a','e','i','o','u','A','E','I','O','U'};
        char[] sArray = s.toCharArray();
        
        
        int left = 0;
        int right = s.length()-1;
        
        while(left < right) {
            
            while(left<s.length()-1 && !isVowel(sArray[left], vowels)) {
                left++;
            }
            
            while(right>=0 && !isVowel(sArray[right], vowels)) {
                right--;
            }
            
            if(left< right){
                
                char temp = sArray[left];
                sArray[left] = sArray[right];
                sArray[right]= temp;
                left++;
                right--;
            }  
        }
        
        return new String(sArray);
             
    }
    
    private boolean isVowel(char c, char[] vowels) {
        for(char v: vowels){
            if(v==c) {
                return true;
            }
        }
        return false;
    }
}