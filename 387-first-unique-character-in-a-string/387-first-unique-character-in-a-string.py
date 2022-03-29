class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dit = {}
        
        for char in s:
            if char not in dit:
                dit[char]=0
            else:
                dit[char]+=1
        
        for i, c in enumerate(s):
            if dit[c]==0:
                return i
        
        return -1
        