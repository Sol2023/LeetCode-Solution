class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int tank = 0;
        for(int i=0; i< gas.length; i++){
            tank+=gas[i]-cost[i];
        }
        if(tank<0) return -1;
        
        int start=0, accumulation=0;
        for(int j=0; j<gas.length; j++){
            int current_gain = gas[j];
            
            if(accumulation+current_gain-cost[j]<0){
                start=j+1;
                accumulation=0;
            }
            else{
                accumulation+=current_gain-cost[j];
            }
        }
        return start;
        
    }
}