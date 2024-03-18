class Solution {
    public int compress(char[] chars) {
        
        int finalIndex=0;
        int index=0;
        
        while(index<chars.length) {
            
            char currentChar = chars[index];
            
            int count=0;
            
            while(index<chars.length && chars[index]==currentChar) {
                index++;
                count++;
            }
            
            chars[finalIndex++] = currentChar;
            
            if(count!=1) {
                for(char c: String.valueOf(count).toCharArray()){
                    
                    chars[finalIndex++]=c;
                    
                }
                    
            }
            
            
        }
        return finalIndex;
    }
}