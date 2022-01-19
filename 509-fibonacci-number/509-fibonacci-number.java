class Solution {
    public int fib(int n) {
        HashMap<Integer, Integer> memorize = new HashMap<Integer, Integer>();
        memorize.put(0,0);
        memorize.put(1,1);
        
        return getNFib(n, memorize);
    }
    
    public int getNFib(int n, HashMap<Integer,Integer> memorize) {
        if(memorize.containsKey(n)){
            return memorize.get(n);
        } else {
            memorize.put(n, getNFib(n-1, memorize)+ getNFib(n-2, memorize));
            return memorize.get(n);
        }
    }
        
}