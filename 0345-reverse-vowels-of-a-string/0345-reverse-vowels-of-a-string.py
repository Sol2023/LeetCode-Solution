class Solution:
    def reverseVowels(self, s: str) -> str:
        
        left =0
        right = len(s)-1
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        
        while left<right:
            
            while left<len(s)-1 and s[left] not in vowels:
                left+=1
            
            while right>=0 and s[right] not in vowels:
                right-=1
                
            if left < right:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
        
        
        return "".join(s)
        