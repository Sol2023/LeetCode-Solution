class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
    
        ditS = {}
        ditT = {}
        
        for i in range(len(s)):
            if s[i] not in ditS:
                ditS[s[i]]=0
            else:
                ditS[s[i]]+=1
         
        for i in range(len(t)):
            if t[i] not in ditT:
                ditT[t[i]]=0
            else:
                ditT[t[i]]+=1
        
        return ditS == ditT
        