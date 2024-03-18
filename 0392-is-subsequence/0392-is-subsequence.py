class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        pivot =0
        
        for char in t:
            
            if pivot==len(s):
                return True
            
            elif s[pivot]==char:
                pivot+=1
                
        return pivot ==len(s)