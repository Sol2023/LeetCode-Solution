class Solution {
    public boolean isPalindrome(String s) {
        int left=0;
        int right = s.length()-1;
        char cLeft;
        char cRight;
        
        while(left< right){
            cLeft = s.charAt(left);
            cRight = s.charAt(right);
            
            if(!Character.isLetterOrDigit(cLeft)){
                left++;
            } else if (!Character.isLetterOrDigit(cRight)){
                right--;
            } else{
                if(Character.toLowerCase(cLeft)!=Character.toLowerCase(cRight)){
                    return false;
                } else{
                    left++;
                    right--;
                }
            
            }
        }
        
        return true;
    }
}