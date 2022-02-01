class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        sequences = {}
        repeatedDNA=[]
        
        for i in range(len(s)-9):
            if s[i:i+10] in sequences:
                sequences[s[i:i+10]]+=1
            else:
                sequences[s[i:i+10]] = 0
        print(sequences)
        for key in sequences:
            if sequences[key]>=1:
                repeatedDNA.append(key)
        
        return repeatedDNA