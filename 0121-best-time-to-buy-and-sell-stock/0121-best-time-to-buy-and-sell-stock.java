class Solution {
    public int maxProfit(int[] prices) {
        
        
//         //brute force
//         int result = 0;
        
//         for(int i=0; i< prices.length-1; i++) {
//             for(int j=i+1; j<prices.length; j++) {
                
//                 result = Math.max(result, prices[j]-prices[i]);
//             }
//         }
//         return result;
        
        int result = 0;
        int min_price = Integer.MAX_VALUE;
        
        for(int price: prices) {
            
            min_price = Math.min(min_price, price);
            result = Math.max(result, price - min_price);
            
        }
        
        return result;
    }
}