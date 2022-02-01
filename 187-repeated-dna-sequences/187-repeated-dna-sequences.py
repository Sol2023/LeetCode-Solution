class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        sequences = {}
        repeatedDNA=[]
        
        for i in range(len(s)-9):
            current = s[i:i+10]
            if current in sequences and current not in repeatedDNA:
                repeatedDNA.append(current)
            else:
                sequences[s[i:i+10]] = 1
        
        
        return repeatedDNA