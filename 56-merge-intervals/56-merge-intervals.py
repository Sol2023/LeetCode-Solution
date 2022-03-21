class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res =[]
        
        intervals.sort(key= lambda x: x[0])
        
        for i in intervals:
            if not res or res[-1][-1] < i[0]:
                res.append(i)
            
            else:
                res[-1][-1] = max(i[-1], res[-1][-1])
                res[-1][0] = min(i[0], res[-1][0])
        
        return res
            