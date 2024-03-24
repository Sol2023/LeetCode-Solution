class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        sets = {'a', 'e', 'i', 'o', 'u'}
        
        res = count =0
        
        for i, c in enumerate(s):
            
            if c in sets:
                
                count+=1
            
            if i>=k and s[i-k] in sets:
                
                count-=1
            
            res = max(res, count)
            
        
        return res
                