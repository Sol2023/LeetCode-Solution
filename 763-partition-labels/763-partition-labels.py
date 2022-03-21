class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterIdx = {c:i for i, c in enumerate(s)}
        
        left =0
        right =0
        result = []
        
        for i, char in enumerate(s):
            right = max(right, letterIdx[char])
            
            if i==right:
                result+=[right-left+1]
                left=i+1
        
        return result
        