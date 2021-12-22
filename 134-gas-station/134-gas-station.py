class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        
        start=0
        accumulation =0
        for i in range(len(gas)):
            current_gain = gas[i]
            
            if (current_gain+accumulation -cost[i])<0:
                start=i+1
                accumulation = 0
            else:
                accumulation+=current_gain-cost[i]
        return start
            
            
            