class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        result = []
        for i in range(len(heights)):
    
            while len(result) and heights[result[-1]]<=heights[i]:
                result.pop()
            result.append(i)
        
        return result
            
        