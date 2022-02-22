class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dit ={}
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        for i, char in enumerate(s):
            dit[char] = i+1
        ans=0
        for i, char in enumerate(columnTitle):
            value = dit[char]
            ans+=value*26**(len(columnTitle[i:])-1)
            
        return ans
        