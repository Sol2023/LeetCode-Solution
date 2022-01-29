class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charCodeS=0
        charCodeT=0
        
        for i in range(len(s)):
            charCodeS+=ord(s[i])
            
        for i in range(len(t)):
            charCodeT+=ord(t[i])
            
        return chr(charCodeT-charCodeS)
        