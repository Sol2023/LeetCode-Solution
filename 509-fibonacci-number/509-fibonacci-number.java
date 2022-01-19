class Solution {
    public int fib(int n) {
        int[] lastTwo =new int[2];
        lastTwo[0] = 0;
        lastTwo[1] = 1;
        int count =2;
        while(count <= n) {
            int nextNum = lastTwo[0] + lastTwo[1];
            lastTwo[0] = lastTwo[1];
            lastTwo[1] = nextNum;
            count++;
        }
        
        return n>0 ? lastTwo[1] : lastTwo[0];
        
    }
    
   
        
}