class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
#         l = min(len(word1), len(word2))
#         index = 0
#         res = []
        
#         while index < l:
#             res.append(word1[index])
#             res.append(word2[index])
#             index+=1
        
#         if index<len(word1):
#             res.append(word1[index:])
            
#         if index<len(word2):
#             res.append(word2[index:])
            
        
#         return "".join(res)
        
    
        result = ""
        for i in range(max(len(word1), len(word2))):
            
            if i < len(word1):
                result+=word1[i]
            
            if i < len(word2):
                result+=word2[i]
                
        
        return result
        
        
        