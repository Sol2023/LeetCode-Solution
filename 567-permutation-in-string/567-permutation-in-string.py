class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
  
        s1 = self.sort1(s1)
        
        for i in range(len(s2)-len(s1)+1):
            if s1 ==self.sort1(s2[i:i+len(s1)]):
                return True
        
        return False
    
    def sort1(self, string):
        s = list(string)
        s.sort()
        
        return s