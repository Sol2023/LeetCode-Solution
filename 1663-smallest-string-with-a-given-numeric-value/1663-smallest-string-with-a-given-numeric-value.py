class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        numA = max(0, (n*26-k-1)//25)
        numM = k-numA-26*(n-numA-1)
        
        return 'a'*numA + chr(96+numM) + 'z'*(n-numA-1)