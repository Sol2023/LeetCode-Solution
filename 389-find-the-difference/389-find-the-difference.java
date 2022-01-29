class Solution {
    public char findTheDifference(String s, String t) {
        int charCodeS = 0;
        int charCodeT = 0;
        
        for(int i =0; i< s.length(); i++){
            charCodeS+= (int)s.charAt(i);
        }
        for(int j = 0; j<t.length(); j++) {
            charCodeT+=(int)t.charAt(j);
        }
        
        return (char)(charCodeT - charCodeS);
    }
}