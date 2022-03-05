class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group=[1]
        
        for i in range(1,len(s)):
            if s[i-1]!=s[i]:
                group+=[1]
            else:
                group[-1]+=1
            
        ans =0
        
        for i in range(1,len(group)):
            ans+=min(group[i-1], group[i])
        
        return ans