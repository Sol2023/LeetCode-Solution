class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        miniCost = 0
        l=(len(costs)+1)//2
        costs.sort(key = lambda x: x[0]-x[1])
        for i in range(l):
            
            miniCost+=costs[i][0]+costs[i+l][1]
        
        return miniCost