class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n>=2:
            if n%2==1:
                matches = (n-1)//2
                advance = 1+matches
                result+=matches
                n= advance
            else:
                matches = n//2
                advance = n//2
                result+=matches
                n= advance
        
        return result